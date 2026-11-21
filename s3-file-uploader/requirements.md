# Requirements Specification - AWS S3 File Uploader
**Student Name**: Abdhan  
**Assessor**: Daniel  
**Date**: 2026-11-21  

## Interview Questions & Assessor Responses
1. **What S3 operations are needed?**  
   *Response:* Create S3 buckets, upload files, list bucket contents, and delete files from a bucket.
2. **What file types and sizes should be supported?**  
   *Response:* Any file type up to a 100 MB limit, validated for existence, size, and read permissions before upload.
3. **How should errors and logging be handled?**  
   *Response:* Clear user-friendly error messages in the console without crashing, plus timestamped entries written to `logs/operations.log`.
4. **How are AWS credentials managed?**  
   *Response:* Stored externally in `config.json` (excluded from Git via `.gitignore`), with a `config.json.example` template provided.
5. **Who are the target users and what documentation is needed?**  
   *Response:* Non-technical small business staff; requires a clear CLI menu, `README.md` setup instructions, code comments, and test/debugging logs.

## Derived Requirements
| Requirement ID | Category | Description | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- |
| FR-001 | Functional | Create S3 bucket by name | High | Bucket created in AWS S3 console |
| FR-002 | Functional | Upload file to S3 bucket | High | File appears in target S3 bucket |
| FR-003 | Functional | List bucket contents | High | Displays filenames and formatted sizes |
| FR-004 | Functional | Delete file from S3 bucket | High | File removed from target S3 bucket |
| FR-005 | Functional | Validate and clean bucket names | Medium | Uppercase/spaces converted to lowercase/hyphens |
| FR-006 | Functional | Log all operations to file | High | Entries appended to `logs/operations.log` |
| SR-001 | Security | Load AWS credentials from JSON config | High | No hardcoded keys; `config.json` gitignored |
| SR-002 | Security | Validate files before upload | High | Rejects missing, unreadable, or >100 MB files |

**Student Signature**: Abdhan **Date**: 2026-11-21  