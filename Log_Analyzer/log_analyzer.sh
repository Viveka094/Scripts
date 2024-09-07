#!/bin/bash

LOG_FILE="./access.log"  # Path to the web server log file
REPORT_FILE="log_report.txt"  # Path to the report file

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Initialize the report file
echo "Log File Analysis Report" > $REPORT_FILE
echo "Generated on: $TIMESTAMP" >> $REPORT_FILE
echo "" >> $REPORT_FILE

# 1. Count the number of 404 errors
echo "1. Number of 404 Errors:" >> $REPORT_FILE
grep ' 404 ' $LOG_FILE | wc -l >> $REPORT_FILE
echo "" >> $REPORT_FILE

# 2. List the most requested pages
echo "2. Most Requested Pages:" >> $REPORT_FILE
awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -nr | head -n 10 >> $REPORT_FILE
echo "" >> $REPORT_FILE

# 3. List IP addresses with the most requests
echo "3. IP Addresses with Most Requests:" >> $REPORT_FILE
awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -nr | head -n 10 >> $REPORT_FILE

# 4. Response codes and their counts
echo "4. HTTP Response Codes and their counts:" >> $REPORT_FILE
awk '{print $9}' $LOG_FILE | sort | uniq -c | sort -nr >> $REPORT_FILE


# Display the report
cat $REPORT_FILE
