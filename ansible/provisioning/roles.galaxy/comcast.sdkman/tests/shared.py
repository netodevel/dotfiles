import re

sdkman_user = 'jenkins'
sdkman_group = 'jenkins'


def script_wrap(host, cmds, as_interactive=True):
    # if running as interactive shell, .bashrc will be sourced
    wrapped_cmd = "/bin/bash {0} -c '{1}'".format(
        '-i' if as_interactive else '',
        '; '.join(cmds)
    )

    if host.user.name == sdkman_user:
        return wrapped_cmd
    else:
        return "sudo -H -u {0} {1}".format(sdkman_user, wrapped_cmd)


def check_run_for_rc_and_result(cmds, expected, host, check_stderr=False,
                                as_interactive=True, regex_match=False):
    result = host.run(script_wrap(host, cmds, as_interactive))
    assert result.rc == 0
    check_stream = result.stderr if check_stderr else result.stdout
    if regex_match:
        regex = re.compile(expected)
        assert regex.match(check_stream)
    else:
        assert check_stream.find(expected) != -1


def test_config_file(host):
    result = host.run(script_wrap(host, ['echo $SDKMAN_DIR']))
    config_file_path = "{0}/etc/config".format(result.stdout.rstrip())

    f = host.file(config_file_path)
    assert f.exists
    assert f.is_file
    assert f.mode in [0o644, 0o654, 0o655]
    assert f.user == sdkman_user
    assert f.group == sdkman_group
    assert f.contains('sdkman_auto_answer=true')


def test_gradle_installed(host):
    cmds = ['gradle --version']
    expected = 'Gradle 6.8.1'
    check_run_for_rc_and_result(cmds, expected, host)


def test_other_gradle_installed(host):
    cmds = ['sdk use gradle 6.7.1', 'gradle --version']
    expected = 'Gradle 6.7.1'
    check_run_for_rc_and_result(cmds, expected, host)


def test_offline(host):
    cmds = ['sdk list gradle']
    expected = 'Offline: only showing installed gradle versions'
    check_run_for_rc_and_result(cmds, expected, host)

    cmds = ['sdk offline disable', 'sdk list gradle']
    expected = 'Available Gradle Versions'
    check_run_for_rc_and_result(cmds, expected, host)
