#!/bin/bash

# Update the package lists and install system updates
sudo yum update -y

# Install Python and necessary packages
sudo yum install python3-pip aws-cli -y
sudo pip3 install flask boto3 flask-cors

# Set up environment variables (adjust as needed for your AWS region or table name)
export AWS_REGION="us-east-1"  # Replace with your AWS region if different
export DYNAMO_TABLE="EventsTable"  # Replace with your DynamoDB table name

# Download the HTML file from S3
S3_BUCKET="jr-28-10"  # Replace with your actual S3 bucket name
aws s3 cp s3://$S3_BUCKET/index.html static/index.html

# Run the Flask application on startup, specifying the host and port
echo "Starting Flask app..."
sudo nohup python3 app.py > app.log 2>&1 &
echo "Flask app started on http://54.234.252.116/"

# Confirm that the app has been deployed
echo "Deployment complete. You can check the app log with: tail -f app.log"
