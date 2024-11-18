#!/bin/bash

# Set your instance ID and S3 bucket name
INSTANCE_ID="<Your Instance ID>"
S3_BUCKET_NAME="<Your S3 Bucket Name>"

# Wait until the EC2 instance is running
echo "Checking if the EC2 instance is running..."
while true; do
    INSTANCE_STATE=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query "Reservations[0].Instances[0].State.Name" --output text)
    if [ "$INSTANCE_STATE" == "running" ]; then
        echo "EC2 instance is running."
        break
    else
        echo "EC2 instance is in state: $INSTANCE_STATE. Waiting..."
        sleep 3  # Wait 3 seconds before checking again
    fi
done

# Retrieve the public IP address of the EC2 instance
PUBLIC_IP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query "Reservations[0].Instances[0].PublicIpAddress" --output text)

# Check if the IP address was retrieved successfully
if [ -z "$PUBLIC_IP" ]; then
    echo "Failed to retrieve the public IP address."
    exit 1
fi

# Define the new URL using the EC2 instance's public IP
URL="http://$PUBLIC_IP"

# Replace the `server` URL in index.html
sed -i "s|^\([[:space:]]*\)const server = 'http://.*';|\1const server = '$URL';|" index.html

# Upload the updated index.html file to the specified S3 bucket
aws s3 cp index.html s3://$S3_BUCKET_NAME/index.html 

echo "index.html updated with IP $PUBLIC_IP and uploaded to S3 bucket $S3_BUCKET_NAME"
