#!/bin/bash

# Check if the bucket name is provided as an argument
if [ -z "thebombbestbucket" ]; then
    echo "Usage: $0 <bucket-name>"
    exit 1
fi

BUCKET_NAME=eventsmanagername

# Check if the bucket exists
if ! aws s3 ls "s3://$BUCKET_NAME" >/dev/null 2>&1; then
    echo "Bucket $BUCKET_NAME does not exist or you do not have access to it."
    exit 1
fi

# Confirm deletion
read -p "Are you sure you want to delete the bucket $BUCKET_NAME and all its contents? (yes/no): " CONFIRMATION
if [[ "$CONFIRMATION" != "yes" ]]; then
    echo "Aborted."
    exit 0
fi

# Empty the bucket
echo "Deleting all objects in the bucket..."
aws s3 rm "s3://$BUCKET_NAME" --recursive

if [ $? -ne 0 ]; then
    echo "Failed to empty the bucket. Please check your permissions and try again."
    exit 1
fi

# Delete the bucket
echo "Deleting the bucket $BUCKET_NAME..."
aws s3api delete-bucket --bucket $BUCKET_NAME

if [ $? -eq 0 ]; then
    echo "Bucket $BUCKET_NAME deleted successfully."
else
    echo "Failed to delete the bucket. Please check your permissions and try again."
    exit 1
fi


