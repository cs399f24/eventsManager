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
- Basic knowledge of Flask, HTML, and JavaScript

---

# CLI Setup Instructions
# Cloud 9 Setup Instructions
##Configure 9 

### Step 1: Set Up the EC2 Instance

1. Launch an EC2 instance (Amazon Linux or Ubuntu recommended).
2. SSH into your instance:
   ```bash
   ssh -i "your-key.pem" ec2-user@your-public-ip
   ```

### Step 2: Clone the Repository

1. Install git:
   ```bash
   sudo yum install git
   ```

2. Clone the GitHub repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/events-manager.git
   ```

3. Change to the working directory:
   ```bash
   cd events-manager
   ```

4. Create Virtual Enviroment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install Python3 pip package:
   ```bash
   sudo yum install python3-pip -y
   ```

6. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

7. Run the Flask app on the instance:
   ```bash
   sudo python3 app.py
   ```
   
   The app should now be running and accessible at `http://your-public-ip/api/events`.

### Step 4: Update Frontend with EC2 IP Address

1. Open `index.html` from the cloned repository and replace the server variable with your EC2 instance’s public IP address:
   ```javascript
   const server = 'http://your-public-ip';
   ```

### Step 5: Host the Frontend on S3

1. Go to your AWS S3 dashboard and create a new bucket.
2. In the **Permissions** tab, enable **public access** and configure **bucket policy** to allow public access to files.
3. Upload `index.html` and all necessary frontend files to your S3 bucket.
4. Enable **Static Website Hosting** in the bucket properties, and note the URL provided for accessing your site.
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

### Step 6: Access the Application

Navigate to the S3 URL from Step 4 to use the application.
