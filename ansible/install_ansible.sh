#!/bin/bash

echo | sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update -y
sudo apt install python3-pip -y
yes | sudo pip3 install pywinrm 
yes | sudo pip3 install pyvmomi 
yes | sudo pip3 install ansible 



