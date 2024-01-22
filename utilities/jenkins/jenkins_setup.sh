#!/bin/bash

public_ipv4=$(curl -s http://checkip.amazonaws.com/)
# Import the repository of Jenkins
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

# Update yum
sudo yum package -y

# Add required dependencies for the jenkins package
# Check for required dependencies
if rpm -q fontconfig; then
  echo "fontconfig already installed, skipping..."
else
  echo "Installing fontconfig..."
  sudo yum install fontconfig -y
fi

if rpm -q java-11-openjdk; then
  echo "java-11-openjdk already installed, skipping..."
else
  echo "Installing java-11-openjdk..."
  sudo yum install java-11-openjdk -y
fi

# Install Jenkins
if rpm -q jenkins; then
  echo "Jenkins already installed, skipping..."
else
  echo "Installing Jenkins..."
  sudo yum install jenkins -y
fi

sudo systemctl daemon-reload

# To check if jenkins is really installed
sudo systemctl status jenkins
# You should see:
# jenkins.service - Jenkins Continuous Integration Server
#    Loaded: loaded (/usr/lib/systemd/system/jenkins.service; disabled; vendor preset: disabled)
#    Active: inactive (dead)

# You can enable the Jenkins service to start at boot with the command:
sudo systemctl enable jenkins

# You can start the Jenkins service with the command:
sudo systemctl start jenkins
# On the Unlock Jenkins page, paste this password into the Administrator password field and click Continue:
cat /var/lib/jenkins/secrets/initialAdminPassword

echo "Server is running at http://$public_ipv4:8080"

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