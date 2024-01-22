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
## Pull Docker Image on Docker Hub
### On EC2 Instance for RMIT Store Apache
***Clean up running ports***
```bash
sudo docker stop $(sudo docker ps -aq)
kill $(lsof -t -i tcp:80)
sudo docker container prune
```
***Run my prepared Docker Image***
```
docker run -d --name my-rmit-store -p 80:80 laansdole/s3963207-rmit-store
```
## Local Docker Build
### To populate data
***Assuming you are on `root` directory***
- Connect your EC2 Instance to AWS RDS Instance (rmit-store)
- On EC2 CentOS, assuming that you are on the root directory of the repository, run following commands:
```bash
sudo mysql -hrmit-store.c9kica0o89u0.us-east-1.rds.amazonaws.com -udb_admin -prmit_password < ./sql-scripts/sql-script.sql
```
You can change `rmit-store.c9kica0o89u0.us-east-1.rds.amazonaws.com` to any other hostname
### Docker Build
***Assuming you are on `utiilities` directory***
```bash
# Build the Docker image from the Dockerfile in the current directory
docker build -t <image_name> .
```
```bash
docker run -d --name my-rmit-store -p 80:80 <image_name>
```
