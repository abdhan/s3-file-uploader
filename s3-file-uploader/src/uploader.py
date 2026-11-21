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

def load_aws_config():
    """Load AWS credentials from config.json."""
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        aws = data["aws"]
        return {
            "region": aws["region"],
            "access_key_id": aws["access_key_id"],
            "secret_access_key": aws["secret_access_key"],
            "session_token": aws.get("session_token"),
        }
    except FileNotFoundError:
        print("Error: config.json not found")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON in config file")
        return None
    except Exception as e:
        print(f"Error loading config file: {e}")
        return None


def test_aws_connection():
    """Verify AWS credentials using STS get_caller_identity."""
    print("Testing AWS connection...")
    config = load_aws_config()
    if config is None:
        print("Failed to load config")
        return False

    try:
        sts = boto3.client(
            "sts",
            region_name=config["region"],
            aws_access_key_id=config["access_key_id"],
            aws_secret_access_key=config["secret_access_key"],
            aws_session_token=config["session_token"],
        )
        response = sts.get_caller_identity()
        print("✓ AWS Connection Successful!")
        print(f"Account: {response['Account']}")
        print(f"ARN: {response['Arn']}")
        return True
    except Exception as e:
        print("✗ AWS Connection Failed")
        print(f"Error: {e}")
        return False

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

def create_s3_client():
    """Initialize and return an authenticated boto3 S3 client."""
    config = load_aws_config()
    if config is None:
        return None
    try:
        return boto3.client(
            "s3",
            region_name=config["region"],
            aws_access_key_id=config["access_key_id"],
            aws_secret_access_key=config["secret_access_key"],
            aws_session_token=config["session_token"],
        )
    except Exception as e:
        print(f"Error creating S3 client: {e}")
        return None


def format_file_size(size_bytes):
    """Format byte size into a human-readable string."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def create_s3_bucket(bucket_name):
    """Create a new S3 bucket."""
    client = create_s3_client()
    if client is None:
        return False
    try:
        clean_name = bucket_name.strip().lower().replace(" ", "-")
        config = load_aws_config()
        region = config["region"] if config else AWS_REGION

        if region == "us-east-1":
            client.create_bucket(Bucket=clean_name)
        else:
            client.create_bucket(
                Bucket=clean_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"✓ Bucket '{clean_name}' created successfully!")
        return True
    except ClientError as e:
        print(f"✗ AWS Error creating bucket: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"✗ Error creating bucket: {e}")
        return False

def upload_file_to_s3(file_path, bucket_name):
    """Validate and upload a file to an S3 bucket."""
    is_valid, message = validate_file(file_path)
    if not is_valid:
        print(f"✗ Validation failed: {message}")
        return False

    client = create_s3_client()
    if client is None:
        return False

    try:
        file_name = os.path.basename(file_path)
        print(f"Uploading '{file_name}' to '{bucket_name}'...")
        client.upload_file(file_path, bucket_name, file_name)
        print(f"✓ File '{file_name}' uploaded successfully!")
        return True
    except ClientError as e:
        print(f"✗ AWS Upload Error: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"✗ Error uploading file: {e}")
        return False

def list_bucket_contents(bucket_name):
    """Retrieve and display all files in an S3 bucket."""
    client = create_s3_client()
    if client is None:
        return

    try:
        response = client.list_objects_v2(Bucket=bucket_name)
        contents = response.get("Contents", [])

        if not contents:
            print(f"Bucket '{bucket_name}' is empty.")
            return

        print(f"\n--- Contents of '{bucket_name}' ---")
        for obj in contents:
            key = obj["Key"]
            size = format_file_size(obj["Size"])
            print(f"  {key} - {size}")
        print("-----------------------------------")
    except ClientError as e:
        print(f"✗ AWS List Error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"✗ Error listing bucket contents: {e}")

def delete_file_from_s3(file_name, bucket_name):
    """Delete a file from an S3 bucket."""
    client = create_s3_client()
    if client is None:
        return False

    try:
        client.delete_object(Bucket=bucket_name, Key=file_name)
        print(f"✓ File '{file_name}' deleted from '{bucket_name}'!")
        return True
    except ClientError as e:
        print(f"✗ AWS Delete Error: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"✗ Error deleting file: {e}")
        return False

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
        bucket_name = input("Enter a unique bucket name: ")
        create_s3_bucket(bucket_name)

    elif choice == "2":
        # Upload file code here
        file_path = input("Enter the path to the file you want to upload: ")
        bucket_name = input("Enter the bucket name: ")
        upload_file_to_s3(file_path, bucket_name)

    elif choice == "3":
        # List contents code here
        bucket_name = input("Enter the bucket name: ")
        list_bucket_contents(bucket_name)

    elif choice == "4":
        # Delete file code here
        bucket_name = input("Enter the bucket name: ")
        file_name = input("Enter the file name: ")
        delete_file_from_s3(file_name, bucket_name)
        
    elif choice == "5":
        # Test AWS connection
        test_aws_connection()

    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

