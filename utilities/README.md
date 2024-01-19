## Getting Started

### On EC2 Instance for RMIT Store Apache

**_Clean up running ports_**

```bash
sudo docker stop $(sudo docker ps -aq)
kill $(lsof -t -i tcp:80)
```

**_Run my prepared Docker Image_**

```
docker run -d --name my-rmit-store -p 80:80 laansdole/s3804811-rmit-store
```

## Local Build

### To populate data

**_Assuming you are on `root` directory_**

- Connect your EC2 Instance to AWS RDS Instance (rmit-store)
- On EC2 CentOS, assuming that you are on the root directory of the repository, run following commands:

```bash
sudo mysql -hrmit-store.c9kica0o89u0.us-east-1.rds.amazonaws.com -udb_admin -prmit_password < ./sql-scripts/sql-script.sql
```

You can change `rmit-store.c9kica0o89u0.us-east-1.rds.amazonaws.com` to any other hostname

### Docker Build

**_Assuming you are on `utiilities` directory_**

```bash
# Build the Docker image from the Dockerfile in the current directory
docker build -t <image_name> .
```

```bash
docker run -d --name my-rmit-store -p 80:80 <image_name>
```
