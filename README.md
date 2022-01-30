# dotfiles

sudo chown -R $USER ansible/

### wsl setup

```sh
exec wsl/setup_wsl.ps1
sudo apt-get install dos2unix

sudo dos2unix ansible/install_ansible.sh
sudo chmod +x install_ansible.sh
./install_ansible.sh
```
### without wsl

```sh
sudo chmod +x install_ansible.sh
./install_ansible.sh
```

### run ansbile tasks

```sh
ansible-playbook ansible/provisioning/playbook.yml --tag "tags_here"
```
