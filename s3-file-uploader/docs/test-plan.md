# Test Plan - S3 File Uploader

**Student Name**: [Your Name]  
**Date**: [Today's Date]  
**Application Version**: 1.0

## Test Objectives

- Verify all S3 operations work correctly
- Validate error handling for invalid inputs
- Test file upload with various file sizes
- Confirm configuration loading works
- Verify logging functionality

## Test Environment

- **Operating System**: [e.g., Windows 11, macOS, Linux]
- **Python Version**: [Run: `python --version`]
- **boto3 Version**: [Run: `pip show boto3`]
- **AWS Region**: us-east-1
- **Test Date**: [Date you run tests]

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
| TC-001 | Create Bucket | Create bucket with valid lowercase name | my-test-bucket | Bucket created successfully | | | |
| TC-002 | Create Bucket | Create bucket with uppercase name | MyTestBucket | Converted to lowercase, bucket created | | | |
| TC-003 | Create Bucket | Create bucket with spaces | My Test Bucket | Spaces replaced with hyphens | | | |
| TC-004 | Upload File | Upload small text file | test-small.txt | Upload successful | | | |
| TC-005 | Upload File | Upload medium file | test-medium.png | Upload successful | | | |
| TC-006 | Upload File | Upload non-existent file | missing.txt | Error: File not found | | | |
| TC-007 | Upload File | Upload file with special chars in name | test-special-chars!@#.txt | Upload successful | | | |
| TC-008 | List Contents | List files in populated bucket | my-test-bucket | Shows all uploaded files | | | |
| TC-009 | List Contents | List files in empty bucket | empty-bucket | Shows "Bucket is empty" | | | |
| TC-010 | Delete File | Delete existing file | test-small.txt | File deleted successfully | | | |
| TC-011 | Delete File | Delete non-existent file | missing.txt | Error handled gracefully | | | |
| TC-012 | Connection Test | Test AWS connection | Option 5 | Shows AWS account info | | | |
| TC-013 | Statistics | Show operation statistics | Option 6 | Displays operation counts | | | |
| TC-014 | Logging | Verify log file created | Check logs/ folder | operations.log exists with entries | | | |
| TC-015 | Config Loading | Start app with valid config | Run application | Loads successfully | | | |
| TC-016 | Config Loading | Start app with missing config | Remove config.json | Error: config not found | | | |

---

## Test Summary

**Total Test Cases**: 16  
**Passed**: [Fill in after testing]  
**Failed**: [Fill in after testing]  
**Success Rate**: [Calculate: passed/total * 100]%

**Testing Duration**: [Start time - End time]

---

## Issues Found

[List any bugs or issues discovered during testing]

1. **Bug #1**: [Copy from Step 9 debugging-log.md - the IndexError in show_operation_stats]
2. [Any other issues discovered during testing]

---

## Performance Observations

**File Upload Times:**
- Small file (< 1KB): [e.g., < 1 second]
- Medium file (1-5MB): [e.g., 2-3 seconds]

**Application Responsiveness:**
- Menu navigation: [e.g., Instant]
- AWS API calls: [e.g., 1-2 seconds average]
- Error messages: [e.g., Displayed immediately]

**Notes:**
- [Any performance issues observed]
- [Resource usage observations]

---

## Recommendations for Future Improvements

1. [Suggestion 1 - e.g., Add progress bar for large file uploads]
2. [Suggestion 2 - e.g., Implement bucket name auto-suggestions]
3. [Suggestion 3 - e.g., Add file size validation before upload starts]

**Known Limitations:**
- Maximum file size: 100MB (configurable)
- Requires active internet connection
- AWS Learner Lab session time limits

---

## Conclusion

[Write 2-3 paragraphs covering:
- Overall assessment of application quality
- Summary of test results (X/16 passed)
- Confidence in the application's reliability
- What you learned from the testing process]

Example:
> The S3 File Uploader has been thoroughly tested with 16 systematic test cases covering all major features. 15 out of 16 tests passed on first execution, with one bug identified and fixed during development (Step 9).
>
> All core functionality works reliably including bucket creation, file upload, listing, deletion, and AWS connection testing. Error handling is robust and provides clear feedback to users.
>
> Through this testing process, I gained confidence that the application handles both normal operations and error conditions appropriately. The systematic approach revealed the importance of testing edge cases like empty buckets and missing files.
>
> This application is ready for use in the AWS Learner Lab environment and demonstrates professional development practices.