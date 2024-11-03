'''
Problem: Implement the viewUserActivityLogs API, which retrieves the activity logs for a specified user through the admin portal.

Type: Function

Function Signature:

def viewUserActivityLogs(username: str, limit: int = 100) -> list:
    pass
Description:

The viewUserActivityLogs API retrieves recent activity logs for a specific user, with an optional limit on the number of logs to return.
Each log contains details about the action performed, timestamp, and IP address.
Input:

username: The username of the user whose activity logs are being retrieved. (string)
limit: The maximum number of log entries to retrieve (default is 100). (integer)
Output:

A list of activity logs, with each entry containing the action performed, timestamp, and IP address.
Sample Input:

logs = viewUserActivityLogs("johndoe", limit=10)
Sample Output:

logs = [
    {"action": "logged_in", "timestamp": "2024-10-20T10:00:00Z", "ip_address": "192.168.1.1"},
    {"action": "updated_profile", "timestamp": "2024-10-20T10:15:00Z", "ip_address": "192.168.1.1"}
]
'''
from datetime import datetime
def viewUserActivityLogs(username: str, limit: int = 100) -> list:
    logs = [
        {"username": username, "action": "logged_in", "timestamp": "2024-10-20T10:00:00Z", "ip_address": "192.168.1.1"},
        {"username": username, "action": "updated_profile", "timestamp": "2024-10-20T10:15:00Z", "ip_address": "192.168.1.1"},
        {"username": username, "action": "logged_out", "timestamp": "2024-10-20T10:20:00Z", "ip_address": "192.168.1.1"},
    ]
    return logs[:limit]
             
print(viewUserActivityLogs("abc", limit=10))