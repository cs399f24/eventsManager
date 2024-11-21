<img width="934" alt="Screenshot 2024-11-08 at 10 06 28 AM" src="https://github.com/user-attachments/assets/717916a2-4b47-42f2-9ee8-65ac864ed72e">

# Events Manager

This is a simple events management application built with Flask for the backend and a static HTML/CSS/JavaScript frontend. 
It allows users to view, add, edit, and delete events. The backend API runs on an AWS EC2 instance, 
and the frontend can be hosted on an S3 bucket.

## Prerequisites

- **AWS Account** (Amazon Web Services)
- **AWS EC2 instance** with a public IP address
- **AWS S3 bucket** for static file hosting
- **AWS DynamioDB** for storing
- **AWS Cloud 9** for an optional integrated development environment
- Basic knowledge of Github, basic AWS services, Flask, HTML, and JavaScript

---
## Configuration
1. Create a folder named eventsManagerApp and open terminal at the folder
2. Install git:
   ```bash
   sudo yum install git
   ```
3. Clone this GitHub repository to your local machine:
   ```bash
   git clone 
   ```

### EC2 Instance Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose EC2 to open the AWS EC2 console
3. Choose Launch Instance
   
   **Instance Name:** ec2EventsManager
   
   **Amazon Machine Image:** Keep Amazon Linux
   
   **Instance Type:** Keep t2.mirco
   
   **Key pair:** select the dropdown and choose vockey
   
   **Security Group:** Select to Allow HTTP traffic from the internet
   
   **Keep the rest of the default settings and choose Launch Instance**
   
5. Once the instance is in the running state, select the instance and then select the actions dropdown. Select Security and then select change security groups. In the slect security groups search bar, type httpssh and select the correct security group. Hit add security group and click save. 
6. Select the instance again and then select the actions dropdown. Select Security and then select Modify IAM role. Click the Choose IAM role dropdown and select LabInstanceProfile. Then, click update IAM role.
7. Lastly, select the instance again and choose the security tab. Scroll down to IAM role and it should say LabRole. Scroll down to Security Groups and it should have the httpssh and the launch-wizard-13 security groups. If you don't have the IAM role or right security groups. Repeat steps 4 through 5. Otherwise, you have successfully created and configured the EC2 instance.


8. Navigate to the EC2 console and select instances. Select the ec2EventsManager instance. Copy the Public IPv4 address.
9. Open terminal at the eventsManagerApp folder you made 
10. Change to the working directory:
   ```bash
   cd eventsManager
   ```
12. Use text editor to change the ec2 to change the ip address in the index.hmtl file
   3. Change to the working directory:
   ```bash
   nano index.hmtl
   ```
   Use the down arrow key to scroll down to where it says const server. Delete everything
   in the paraphrases after the http:// and paste the ec2EventsManager Public IPv4 address. Select
   control+x to exit and then click y to save. Click enter to fully exit text editor.
  

### S3 Bucket Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose S3
3. Open the S3 console 
4. Select create a bucket
   
   **Bucket Name:** eventsManagerS3Bucket <add today's date (ex. eventsmanager_s3bucket-     XX-XX-XX)>
   
   In the Permissions tab, enable public access and configure bucket policy to allow
   public access to files. Select the ackowledgement statement. Then select create
   bucket. 
   
6. Navigate the S3 Console to buckets and select the bucket you just created.
7. Navigate to and select Permissions tab.
8. Scroll down to Bucket Policy and click edit
9. Paste this bucket policy
  ```bash
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}
```
   **Click save changes**
   
10. Select upload and upload the index.hmtl from the eventsManagerApp folder you created. Once uploaded click upload at the bottom. You have sucessfuly created and configured the S3 bucket.

### DynamioDB Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose DynamoDB to open the AWS DynamoDB console
3. Select create table
   
   **Name:** EventsTable

   **Partition Key:** event_id

   **Keep Default Settings and select Create Table**

4. You have sucessfully created and configured a DynamioDB table


## Deloyment
### CLI Setup Instructions
1. Open a terminal window on your local machine
2. SSH into the EC2 instance you lanched. Add the Public IPv4 address of the ec2EventsManager.  Repeat step 8 of the EC2 instance configuartion if you need to copy the Public IPv4 address.
   ```bash
   ssh -i labsuser.pem ec2-user@your-public-ip
   ```
3. Install git:
   ```bash
   sudo yum install git
   ```
5. Clone this GitHub repository to your local machine:
   ```bash
   git clone 
   ```
   When prompted, type y 
5. Change to the working directory:
   ```bash
   cd eventsManager
   ```
6. Create Virtual Enviroment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
7. Give permissions to and run the deploybot.sh cript
   ```bash
   chmod +x ./deploybot.sh
   python ./deploybot.sh
   ```
8. The app should now be running and accessible at `http://your-public-ip/api/events`.
    Repeat steps 1-3 of the S3 configuration.
9. Navigate to your S3 bucket and select properties.

10. Scroll down and copy the Bucket website endpoint
11. Paste the url into a browser and the application will run.
    
12. To stop the application in the cloud 9 terminal window, run this command in the terminal
   ```bash
   python ./down.sh
   ```
   The applicaton will stop work now


### Cloud 9 Setup Instructions
1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose Cloud 9 to open the AWS Cloud 9 console
3. Select create environment
   
   **Name:** eventsManger_Cloud9  <add today's date (ex.  eventsManger_Cloud9-XX-XX-XX)>

   **Scroll to network setting and select the secure shell option**

   **Select Create**
   
4. Select and open the Cloud9 environment your just created
5. In terminal window where it says voclabs:~/environment $
   Clone this GitHub repository to your local machine:
   ```bash
   git clone 
   ```
6. Under the eventsManager File directory, select index.hmtl and scroll down to where it
   says const server. Delete everything in the paraphrases after the http:// and paste the ec2EventsManager Public IPv4 address. Repeat step 8 of the EC2 instance configuration if you need to copy the Public IPv4 address.
7. Under the eventsManager File directory, select deploybot.sh
8. Replace the url after the http:// on line 21 with the Public IPv4 address of the ec2EventsManager
9. Replace jr-28-10 with the name of the bucket you created for this application. if you need to copy the name of the bucket. Repeat steps 1-3 of the S3 configuration and then copy the name of the bucket you created
10. In the termnal window where you clone the git repo. Change to the working directory:
   ```bash
   cd eventsManager
   ```
11. Create Virtual Enviroment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
12. Give permissions to and run the deploybot.sh cript
   ```bash
   chmod +x ./deploybot.sh
   python ./deploybot.sh
   ```
13. The app should now be running and accessible at `http://your-public-ip/api/events`.
    Repeat steps 1-3 of the S3 configuration.
14. Navigate to your S3 bucket and select properties.

15. Scroll down and copy the Bucket website endpoint
16. Paste the url into a browser and the application will run.
    
17. To stop the application in the cloud 9 terminal window, run this command in the terminal
   ```bash
   python ./down.sh
   ```
   The applicaton will stop work now

