# AnsiblePlaybookDockerPythonApp
Ansible Playbook that runs on localhost which is a CentOS 7 VM and Install Docker then build a python docker image



Run Ansible Playbook in Docker - Python A

This is an extremely simple Docker example to help introduce you to managing Docker containers via Ansible.

CentOS 7 Ansible  Image

Build Status Docker Automated build

CentOS 7 Docker container for Ansible playbook 

Tags

python3: Latest stable version of Ansible, but on Python 3.8.x.

How to Build
If you need to build the image on your own locally, do the following:

Install Docker.
cd into this directory.
Run docker build -t centos7-ansible .

How to Use
Install Docker.
Pull this image from Docker Hub: docker pull centos7-ansible:latest


$ ansible-playbook -i hosts main.yml
After a minute or so, Ansible will have built and run a container, built from the included Dockerfile.


About the Author

This project was created by Olufemi Aiyeku
