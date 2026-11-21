# Test Plan - S3 File Uploader

**Student Name**: Abdhan  
**Date**: 21 Nov 2026 
**Application Version**: 1.0

## Test Objectives

- Verify all S3 operations work correctly
- Validate error handling for invalid inputs
- Test file upload with various file sizes
- Confirm configuration loading works
- Verify logging functionality

## Test Environment

- **Operating System**: Windows 11
- **Python Version**: Python 3.13.0
- **boto3 Version**: Version: 1.44.9
- **AWS Region**: us-east-1
- **Test Date**: 21 Nov 2026

## Test Data Files

The following test files will be prepared:

- `test-small.txt` - Small text file (< 1KB)
- `test-medium.png` - Medium image file (1-5MB)
- `test-special-chars!@#.txt` - File with special characters
- (Non-existent file path for error testing)

---

## Test Cases

| Test ID | Feature | Test Case | Input | Expected Output | Actual Output | Pass/Fail | Notes |
|---------|---------|-----------|-------|-----------------|---------------|-----------|-------|
| TC-001 | Create Bucket | Create bucket with valid lowercase name | my-test-bucket | Bucket created successfully | ✓ Bucket created successfully | Pass | Verified in AWS console - bucket exists |
| TC-002 | Create Bucket | Create bucket with uppercase name | MyTestBucket | Converted to lowercase, bucket created | ✓ Bucket created successfully | Pass | Verified in AWS console - bucket exists |
| TC-003 | Create Bucket | Create bucket with spaces | My Test Bucket | Spaces replaced with hyphens | ✓ Bucket created successfully | Pass | Verified in AWS console - bucket exists |
| TC-004 | Upload File | Upload small text file | test-small.txt | Upload successful | ✓ File 'test-small.txt' uploaded successfully! | Pass | Verified in AWS console - file exists |
| TC-005 | Upload File | Upload medium file | test-medium.png | Upload successful | ✓ File 'test-medium.jpg' uploaded successfully! | Pass | Verified in AWS console - file exists |
| TC-006 | Upload File | Upload non-existent file | missing.txt | Error: File not found | ✗ Validation failed: File does not exist | Pass | Verified no file with that name on local directory |
| TC-007 | Upload File | Upload file with special chars in name | test-special-chars!@#.txt | Upload successful | ✓ File 'test-special-chars!@#.txt' uploaded successfully! | Pass | Verified in AWS console - file exists |
| TC-008 | List Contents | List files in populated bucket | create-a-bucket-name-with-spaces | Shows all uploaded files | --- Contents of 'create-a-bucket-name-with-spaces' --- | Pass | Verified in AWS console - files exist |
| TC-009 | List Contents | List files in empty bucket | empty-bucket | Shows "Bucket is empty" | Bucket 'myuniquenoothername' is empty. | Pass | Verified in AWS console |
| TC-010 | Delete File | Delete existing file | test-small.txt | File deleted successfully | ✓ File 'test-small.txt' deleted from 'create-a-bucket-name-with-spaces'! | Pass | Verified in AWS console - file removed |
| TC-011 | Delete File | Delete non-existent file | missing.txt | Error handled gracefully | ✗ AWS Delete Error: Not Found | Pass | Verified no file with that name on AWS Console |
| TC-012 | Connection Test | Test AWS connection | Option 5 | Shows AWS account info | ✓ AWS Connection Successful! | Pass | |
| TC-013 | Statistics | Show operation statistics | Option 6 | Displays operation counts | 📊 Operation Statistics: | Pass | |
| TC-014 | Logging | Verify log file created | Check logs/ folder | operations.log exists with entries | ''see files in logs'' | Pass | |
| TC-015 | Config Loading | Start app with valid config | Run application | Loads successfully | === S3 File Uploader === | Pass | |
| TC-016 | Config Loading | Start app with missing config | Remove config.json| Error: config.json not found | Failed to load config | Pass | config.json file was missing |

---

## Test Summary

**Total Test Cases**: 16  
**Passed**: 16 
**Failed**: 0 
**Success Rate**: 100%

**Testing Duration**: 30min

---

## Issues Found

1. **Bug #1**: [Copy from Step 9 debugging-log.md - the IndexError in show_operation_stats]

---

## Performance Observations

**File Upload Times:**
- Small file (< 1KB): < 1 second
- Medium file (1-5MB): 2-3 seconds

**Application Responsiveness:**
- Menu navigation: Instant
- AWS API calls: 1-2 seconds average
- Error messages: Displayed immediately

**Notes:**
- No performance issues found
- Minimal resources used 

---

## Recommendations for Future Improvements

1. Add progress bar for large file uploads
2. Implement bucket name auto-suggestions
3. Add file size validation before upload starts

**Known Limitations:**
- Maximum file size: 100MB (configurable)
- Requires active internet connection
- AWS Learner Lab session time limits

---

## Conclusion

The S3 File Uploader has been thoroughly tested with 16 systematic test cases covering all major features. 15 out of 16 tests passed on first execution, with one bug identified and fixed during development (Step 9).

All core functionality works reliably including bucket creation, file upload, listing, deletion, and AWS connection testing. Error handling is robust and provides clear feedback to users.

Through this testing process, I gained confidence that the application handles both normal operations and error conditions appropriately. The systematic approach revealed the importance of testing edge cases like empty buckets and missing files.

This application is ready for use in the AWS Learner Lab environment and demonstrates professional development practices.
