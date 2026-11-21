"""
AWS S3 File Uploader
Manages file uploads and S3 bucket operations
Student name: # Abdhan
Student ID: # 20164983
"""

import boto3
import os
import json
import datetime
from botocore.exceptions import ClientError

# Configuration
AWS_REGION = "us-east-1"  # Global configuration
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB limit

def validate_file(file_path):
    # Check file exists
    if not os.path.exists(file_path):
        return False, "File does not exist"

    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        return False, f"File too large: {file_size} bytes"

    # Check file is readable
    if not os.access(file_path, os.R_OK):
        return False, "File is not readable"

    return True, "File is valid"

def create_s3_bucket(bucket_name):
    """Create S3 bucket"""
    # Implementation here
    pass

def upload_file_to_s3(file_path, bucket_name):
    """Upload file with error handling"""
    # Implementation here
    pass

def list_bucket_contents(bucket_name):
    """List S3 bucket files"""
    # Implementation here
    pass

# Main program - Menu interface starts here
while True:
    print("\n=== S3 File Uploader ===")
    print("1. Create S3 bucket")
    print("2. Upload file")
    print("3. List bucket contents")
    print("4. Delete file")
    print("5. Test AWS connection")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        # Create bucket code here
        pass
    elif choice == "2":
        # Upload file code here
        pass
    elif choice == "3":
        # List contents code here
        pass
    elif choice == "4":
        # Delete file code here
        pass
    elif choice == "5":
        # Test AWS connection
        pass
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")