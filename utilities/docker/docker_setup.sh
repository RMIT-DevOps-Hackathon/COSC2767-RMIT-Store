#!/bin/bash

# Install Docker
if rpm -q docker; then
  echo "docker already installed, skipping..."
else
  echo "Installing docker..."
  sudo yum install docker -y
fi

# Add group membership for the default ec2-user 
# so you can run all docker commands without using the sudo command
sudo usermod -a -G docker ec2-user

# Run subsequent commands in the current shell without using newgrp
(
  # Enable docker service at AMI boot time and start docker service
  sudo systemctl enable --now docker.service
  sudo systemctl start docker.service
  service docker status
)

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
