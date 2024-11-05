'''
Instructions for API 4:
Problem: Implement the viewSystemStatus API, which allows an administrator to retrieve the current status of the Osiris platform.

Type: Function

Function Signature:

def viewSystemStatus() -> dict:
    pass
Description:

The viewSystemStatus API retrieves key metrics and system health information, including CPU usage, memory usage, active services, and any system alerts.
The function returns a dictionary containing the current system status.
Input:

None
Output:

A dictionary containing system metrics (e.g., cpu_usage, memory_usage, active_services, alerts).
Sample Input:

status = viewSystemStatus()
Sample Output:

status = {
    "cpu_usage": "40%",
    "memory_usage": "70%",
    "active_services": ["auth", "database", "message_queue"],
    "alerts": []
}
'''

import psutil

#retrieve system metrics: cpu usage as a %, memory usage as a %
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory([2])

#make list of active services by iterating through and storing process name
services_list = []
for process in psutil.process_iter():
    services_list.append(process.name())

def viewSystemStatus():
    status = {
        "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "active_services": services_list,
    "alerts": []
    }
    return status