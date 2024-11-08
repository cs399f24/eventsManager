
# Events Manager

This is a simple events management application built with Flask for the backend and a static HTML/CSS/JavaScript frontend. 
It allows users to view, add, edit, and delete events. The backend API runs on an AWS EC2 instance, 
and the frontend can be hosted on an S3 bucket.

## Prerequisites

- **AWS Account** (for EC2 and S3 services)
- **AWS EC2 instance** with a public IP address
- **AWS S3 bucket** for static file hosting
- Basic knowledge of Flask, HTML, and JavaScript

---

## Setup Instructions

### Step 1: Clone the Repository

1. Clone the GitHub repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/events-manager.git
   cd events-manager
   ```

### Step 2: Set Up the EC2 Instance

1. Launch an EC2 instance (Amazon Linux or Ubuntu recommended).
2. SSH into your instance:
   ```bash
   ssh -i "your-key.pem" ec2-user@your-public-ip
   ```

3. Install Python dependencies:
   ```bash
   pip3 install Flask Flask-CORS
   ```

4. Run the Flask app on the instance:
   ```bash
   sudo python3 app.py
   ```
   
   The app should now be running and accessible at `http://your-public-ip/api/events`.

### Step 3: Update Frontend with EC2 IP Address

1. Open `index.html` from the cloned repository and replace the server variable with your EC2 instance’s public IP address:
   ```javascript
   const server = 'http://your-public-ip';
   ```

### Step 4: Host the Frontend on S3

1. Go to your AWS S3 dashboard and create a new bucket.
2. In the **Permissions** tab, enable **public access** and configure **bucket policy** to allow public access to files.
3. Upload `index.html` and all necessary frontend files to your S3 bucket.
4. Enable **Static Website Hosting** in the bucket properties, and note the URL provided for accessing your site.

### Step 5: Access the Application

Navigate to the S3 URL from Step 4 to use the application.
