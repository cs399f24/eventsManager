<img width="1128" alt="Screenshot 2024-11-21 at 8 34 51 PM" src="https://github.com/user-attachments/assets/cc13db37-8318-4a58-8763-4c52965b9831">

# Events Manager

This is a simple events management application built with Flask for the backend and a static HTML/CSS/JavaScript frontend. 
It allows users to view, add, edit, and delete events. The backend API runs on an AWS EC2 instance, the data for events is stored in database in DynamioDB, actions in the UI trigger a SNS notification to an email address and the frontend is be hosted on an S3 bucket.

## Prerequisites

- **AWS Account** (Amazon Web Services)
- **AWS EC2 instance** with a public IP address
- **AWS S3 bucket** for static file hosting
- **AWS DynamioDB** for storing
- **AWS SNS** for email notifications
- **AWS Cloud 9** for an optional integrated development environment
- Basic knowledge of Github, basic AWS services, Flask, HTML, and JavaScript
- an email address

---
## Configuration

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
   
4. Once the instance is in the running state, select the instance and then select the actions dropdown. Select Security and then select change security groups. In the select security groups search bar, type httpssh and select the correct security group. Hit add security group and click save. 
5. Select the instance again and then select the actions dropdown. Select Security and then select Modify IAM role. Click the Choose IAM role dropdown and select LabInstanceProfile. Then, click update IAM role.
6. Lastly, select the instance again and choose the security tab. Scroll down to IAM role and it should say LabRole. Scroll down to Security Groups and it should have the httpssh and the launch-wizard-13 security groups. If you don't have the IAM role or right security groups. Repeat steps 4 through 5. Otherwise, you have successfully created and configured the EC2 instance.

### S3 Bucket Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose S3
3. Open the S3 console 
4. Select create a bucket
   
   **Bucket Name:** eventsManagerS3Bucket <add today's date (ex. eventsmanager_s3bucket-XX-XX-XX)>
   
   In the Permissions tab, enable public access and configure bucket policy to allow
   public access to files. Select the ackowledgement statement. Then select create
   bucket. 
   
5. Navigate the S3 Console to buckets and select the bucket you just created.
6. Navigate to and select Permissions tab.
7. Scroll down to Bucket Policy and click edit
8. Paste this bucket policy
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
   
   You have sucessfuly created and configured the S3 bucket.

### DynamioDB Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose DynamoDB to open the AWS DynamoDB console
3. Select create table
   
   **Name:** EventsTable

   **Partition Key:** event_id

   **Keep Default Settings and select Create Table**

   You have sucessfully created and configured a DynamioDB table

### SNS Configuration

1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose Simple Notification Service to open the AWS SNS console
3. Select Topics
4. Select Create Topic
   Change the FIFO to Standard
   Name: EventsManagerNotifications
   Select Create Topic
5. Select EventsManagerNotifications
6. Select Create Subscription
7. Under Protocol, select email
8. Under Endpoint, enter in the desired email address to be notified
9. Select Create Subscription
10. In email inbox, confirm subscription to SNS

## Deloyment

### Cloud9 Setup Instructions
1. Open AWS Managment Console
2. In the search box to the top right of AWS Managment Console, search for and choose Cloud 9 to open the AWS Cloud9 console
3. Select create environment
   
   **Name:** eventsManger_Cloud9  <add today's date (ex.  eventsManger_Cloud9-XX-XX-XX)>

   **Scroll to network setting and select the secure shell option**

   **Select Create**
   
4. Select and open the Cloud9 environment your just created
5. Select the drop down arrow for the name of the Cloud9. Select the drop down arrow for eventsManager. Select the update_index.sh file.
6. Paste the name of the bucket and the IPv4 address of the EC2 instance you created
7. Select the file named app.py and change line 20 in the app.py file for topic ARN for the SNS
8. In terminal window where it says voclabs:~/environment $
   Clone this GitHub repository to your local machine:
   ```bash
   git clone 
   ```
   
9. Change to the working directory:
   ```bash
   cd eventsManager
   ```
   
11. Create Virtual Enviroment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

12. Run update_index.sh
   3. Change to the working directory:
   ```bash
   chmod +x update_index.sh
   ./update_index.sh 
   ```

12. Give permissions to and run the deploybot.sh script
   ```bash
   chmod +x ./deploybot.sh
   python ./deploybot.sh
   ```
13. The app should now be running and accessible at `http://your-public-ip/api/events`.
    Repeat steps 1-3 of the S3 configuration.
    
15. Navigate to your S3 bucket and select properties.

16. Scroll down and copy the Bucket website endpoint
17. Paste the url into a browser and the application will run.
    
18. To stop the application in the cloud 9 terminal window, run this command in the terminal. This will give permissions to and run the /down.sh script
   ```bash
    chmod +x ./down.sh
   ./down.sh
   ```
   The applicaton will stop working now

