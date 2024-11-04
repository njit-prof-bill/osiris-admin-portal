from datetime import datetime
import socket
def viewUserActivityLogs(username: str, limit: int = 100) -> list:
    time = datetime.utcnow() 
    formattedTime = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    user = socket.gethostname()
    ip_address = socket.gethostbyname(user)
    logs = [
        {"username": username, "action": "logged_in", "timestamp": formattedTime, "ip_address": ip_address},        
        {"username": username, "action": "updated_profile", "timestamp": formattedTime, "ip_address": ip_address},
        {"username": username, "action": "logged_out", "timestamp": formattedTime, "ip_address": ip_address },
    ]
    for i in logs:
        print(i)
    return ""
             
print(viewUserActivityLogs("abc", limit=10))