# API 9: Manage Service Command
# States Schema
#    auth: running/stopped
#    database: running/stopped
#    message_queue: running/stopped

service_states = {
    "auth": "stopped",
    "database": "stopped",
    "message_queue": "stopped"
}

def manageService(service_name: str, action: str) -> bool:
    if service_name not in service_states:
        print(f"Error: Service '{service_name}' does not exist.")
        return False
    
    if action not in ["start", "stop", "restart"]:
        print(f"Error: Invalid action '{action}'. Action must be 'start', 'stop', or 'restart'.")
        return False
    
    if action == "start":
        if service_states[service_name] == "running":
            print(f"Service '{service_name}' is already running.")
            return False
        service_states[service_name] = "running"
        print(f"Service '{service_name}' started successfully.")
    elif action == "stop":
        if service_states[service_name] == "stopped":
            print(f"Service '{service_name}' is already stopped.")
            return False
        service_states[service_name] = "stopped"
        print(f"Service '{service_name}' stopped successfully.")
    elif action == "restart":
        service_states[service_name] = "running"
        print(f"Service '{service_name}' restarted successfully.")
    return True

# Testing the function
print(manageService("auth", "start"))     # True, with "Service 'auth' started successfully."
print(manageService("auth", "restart"))   # True, with "Service 'auth' restarted successfully."
print(manageService("database", "stop"))  # Expected Output: True, with "Service 'database' stopped successfully."
print(manageService("database", "start")) # Expected Output: True, with "Service 'database' started successfully."
print(manageService("cache", "start"))    # Expected Output: False, with "Error: Service 'cache' does not exist."
print(manageService("auth", "pause"))     # Expected Output: False, with "Error: Invalid action 'pause'."
