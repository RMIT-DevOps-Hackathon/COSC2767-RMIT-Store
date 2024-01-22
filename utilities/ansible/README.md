## Acknowledgement
```
# RMIT University Vietnam
#  Course: COSC2767 Systems Deployment and Operations
#  Semester: 2023C
#  Assessment: Assignment 3
#  Author - ID: 
#    Do Le Long An - s3963207
#    La Tran Hai Dang - s3836605
#    Pham Quang Man - s3804811
#    Huynh Van Anh - s3836320
#    Hoang Ngoc Duan - s3817747
#  Created date: 06/01/2024
#  Last modified: 22/01/2024
#  Acknowledgement: RMIT Canvas, ChatGPT, AWS Documentation, StackOverflow,
#  AWSAcademy Learner Lab, GitHub Documentation, Docker Documentation
#  Jenkins Documentation, Tom Huynh
```
## Getting Started
Assuming that you have launched the instance from the CloudFormation YAML file
### On RMIT Store (Apache) Server
***On root user `sudo su -`:***
```bash
rm -f /etc/ansible/hosts
touch /etc/ansible/hosts
echo "
[dockerserver]
[<docker_server_private_ip_address>]
" >> /etc/ansible/hosts
```
***On ansibleadmin user `sudo su - ansibleadmin`:***
```bash
ssh-keygen -t ed25519 -C "dolelongan@gmail.com" -f ~/.ssh/id_ed25519 -N ""
```
```bash
ssh-copy-id [<docker_server_private_ip_address>]
```
- Make sure that apachePlaybook.yml is on the `~` directory
```bash
ansible-playbook apachePlaybook.yml
```
### On Kubectl Server
```bash
rm -f /etc/ansible/hosts
touch /etc/ansible/hosts
echo "
[kubctlserver]
[<kubectl_server_private_ip_address>]
" >> /etc/ansible/hosts
```
***On ansibleadmin user `sudo su - ansibleadmin`:***
```bash
ssh-keygen -t ed25519 -C "dolelongan@gmail.com" -f ~/.ssh/id_ed25519 -N ""
```
```bash
ssh-copy-id [<kubectl_server_private_ip_address>]
```
- Make sure that kubectlPlaybook.yml is on the `~` directory
```bash
ansible-playbook kubectlPlaybook.yml
```



