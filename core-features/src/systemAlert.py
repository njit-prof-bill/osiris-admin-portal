'''Problem: Implement the setSystemAlert API, which allows administrators to create a system-wide alert through the admin portal.

Type: Function

Function Signature:

def setSystemAlert(message: str, priority: str) -> bool:
    pass
Description:

The setSystemAlert API creates a system-wide alert that notifies users and administrators of critical events or issues.
The function takes a message and a priority level (e.g., "low", "medium", "high").
Input:

message: The alert message to display. (string)
priority: The priority level of the alert (e.g., low, medium, high). (string)
Output:

True if the system alert is successfully created, False otherwise.
Sample Input:

response = setSystemAlert("Database maintenance scheduled at 12:00 PM.", "high")
Sample Output:

response = True'''

def setSystemAlert(message: str, priority: str) -> bool:
    if priority != "low" or priority != "medium" or priority != "high":
        return False
    if len(message) == 0:
        return False
    else:
        return True