# System Health Monitoring Script
# Overview
This Python script monitors the system's health by checking key system metrics such as CPU usage, memory usage, disk usage and the number of running processes. If any metric exceeds a predefined threshold, the script will log an alert and print the message on the console.

# Key Features:
1. **CPU Monitoring**: Checks the CPU usage and alerts if it exceeds a set threshold.
2. **Memory Monitoring**: Monitors memory usage and triggers an alert when usage is high.
3. **Disk Monitoring**: Verifies disk space usage and logs an alert if the usage is above the threshold.
4. **Process Monitoring**: Counts the number of active processes and alerts if the count exceeds the defined limit.
5. **Logging**: Writes detailed logs to a file (system_health.log) and outputs messages to the console.
# Prerequisites
* **Python 3.x**: Ensure Python is installed on your system.
* **psutil module**: This script requires the psutil module, which can be installed using the following command:
```
pip install psutil
```
# Setup and Configuration
1. **Download the Script**: Download or clone the Python script to your local machine.
2. **Modify the Thresholds if needed**:

  * The default threshold values are set in the script:
      * CPU_THRESHOLD = 80: Alerts when CPU usage exceeds 80%.
      * MEMORY_THRESHOLD = 80: Alerts when memory usage exceeds 80%.
      * DISK_THRESHOLD = 80: Alerts when disk usage exceeds 80%.
      * PROCESS_THRESHOLD = 300: Alerts when the number of running processes exceeds 300.
  * You can modify these thresholds as needed for your environment.
3. **Run the Script**: Execute the script by running the following command in the terminal or command prompt:

```
python system_health_monitor.py
```
# Output
* **Console Output**: Alerts will be printed directly in the console if any thresholds are exceeded.
* **Log File**: The system health report and any alerts will be written to the system_health.log file, located in the same directory as the script.
# Sample Log Output
The log file (system_health.log) will contain entries similar to the following:

![image](https://github.com/user-attachments/assets/75eb71bf-ce30-4247-92d5-5be75628de1e)

# Sample Console Output

![image](https://github.com/user-attachments/assets/281c0a29-7a7c-4353-ade9-480c526a4838)

# Customization
* **Log File Location**: By default, the log file is stored in the same directory as the script. If you want to change the log file path, modify the following line in the script:
```
log_file_path = os.path.join(current_dir, 'system_health.log')
```
