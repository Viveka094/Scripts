# Log File Analyzer Script
# Overview
This bash script analyzes a web server log file to generate a report on various patterns, including 404 errors, most requested pages, IP addresses with the most requests, and HTTP response codes. It creates a summary report in a text file and displays it on the console.

# Script Details
# Features
1. **Count of 404 Errors**: Counts the number of 404 (Not Found) errors in the log file.
2. **Most Requested Pages**: Lists the most requested pages based on URL.
3. **IP Addresses with Most Requests**: Lists IP addresses that made the most requests.
4. **HTTP Response Codes and Counts**: Lists all HTTP response codes and their frequencies.
# Prerequisites
  * **Log File**: The script requires a web server log file (e.g., access.log).
  * **Bash**: Ensure that you have a bash shell available on your system.
# Script Usage
1. **Save the Script**: Save the provided bash script to a file, for example, log_analyzer.sh.
2. **Set Permissions**: Make the script executable by running:

```
chmod +x log_analyzer.sh
```
3. **Modify Variables**: Edit the script to set the correct path for LOG_FILE and REPORT_FILE variables if needed.
4. **Run the Script**: Execute the script by running:
```
./log_analyzer.sh
```
# Variables
  * **LOG_FILE**: Path to the web server log file. Modify this variable in the script if your log file is located elsewhere.
  * **REPORT_FILE**: Path where the report will be generated. The default is log_report.txt.
# Example Output
After running the script, you will get a report similar to the following in log_report.txt:

![image](https://github.com/user-attachments/assets/3b41c816-8882-4301-9ddb-e6b0c4b70e8e)

# Notes
* The script assumes that the log file uses common log format where:
  * The URL is the 7th field.
  * The IP address is the 1st field.
  * The response code is the 9th field.
* Adjust the script if your log file format differs.
