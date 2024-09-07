import psutil
import logging
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
log_file_path = os.path.join(current_dir, 'system_health.log')


# Configure logging to output messages to both console and a log file
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s %(message)s')

# Define the predefined thresholds for alerts
CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  
PROCESS_THRESHOLD = 300  

# Check CPU usage
cpu_usage = psutil.cpu_percent(interval=1) 
if cpu_usage > CPU_THRESHOLD:  
    logging.info(f"ALERT: High CPU usage detected! CPU Usage: {cpu_usage}%")  
    print(f"ALERT: High CPU usage detected! CPU Usage: {cpu_usage}%")  

# Check Memory usage
memory_info = psutil.virtual_memory()  
memory_usage = memory_info.percent  
if memory_usage > MEMORY_THRESHOLD:  
    logging.info(f"ALERT: High Memory usage detected! Memory Usage: {memory_usage}%") 
    print(f"ALERT: High Memory usage detected! Memory Usage: {memory_usage}%") 

# Check Disk usage
disk_usage = psutil.disk_usage('/').percent 
if disk_usage > DISK_THRESHOLD:  
    logging.info(f"ALERT: High Disk usage detected! Disk Usage: {disk_usage}%")  
    print(f"ALERT: High Disk usage detected! Disk Usage: {disk_usage}%")  

# Check the number of running processes
process_count = len(psutil.pids())  
if process_count > PROCESS_THRESHOLD:  
    logging.info(f"ALERT: High number of running processes detected! Process Count: {process_count}") 
    print(f"ALERT: High number of running processes detected! Process Count: {process_count}")  

# Print a summary report of the system's health
logging.info(f"System Health Report: CPU={cpu_usage}%, Memory={memory_usage}%, Disk={disk_usage}%, Processes={process_count}")
print(f"System Health Report: CPU={cpu_usage}%, Memory={memory_usage}%, Disk={disk_usage}%, Processes={process_count}")
