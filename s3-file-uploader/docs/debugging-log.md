## Bug #1: show_operation_stats() crashes with IndexError

**Date Found**: 21 Nov 2026

**How to Reproduce**:
1. Perform a few S3 operations to populate log
2. Choose choice 6 to see statistics
3. Error is displayed while trying to display statistics

**Expected Behavior**: 
It should give the total no. of operations with a list of each type of operation

**Actual Behavior**: 
It gave a list of operations but when it came to count the total operations it would desplay the below error.

**Error Message/Output**:
❌ Error reading statistics: list index out of range

**Debugging Process**:
1. Added print statements to trace execution

**Root Cause**: 
Statement was trying to access a non existing index in the list. A list starts at 0 and the statement counted from 0

**Fix Applied**:
print(f"\nMost recent operation: {operations[len(operations) - 1]}")


**Testing After Fix**:
📊 Operation Statistics:
Total operations performed: 13

Operation breakdown:
  Creates: 3
  Uploads: 3
  Lists: 4
  Deletes: 3

**Commit**: "Fix: Correct list index in show_operation_stats - Fixes #1"

**GitHub Issue**: #1

---