<p align="center">
  <h2 align="center">netodevel dotfiles</h2>
  <p align="center">Config files for ideavim, vim, vscode, tmux, wsl, ansible and more</p>
</p>


### Dependencies

    - python3

#### Install Ansible

```sh
sudo chmod +x install_ansible.sh
./install_ansible.sh
```

**macosx**
```
brew install ansible
```

#### Ansible dependencies
```sh
ansible-galaxy install -r requirements.yml
```

#### Run Tasks
```sh
ansible-playbook ansible/provisioning/playbook.yml --tag "tags_here"
```
