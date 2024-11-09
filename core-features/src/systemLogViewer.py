import csv

def viewSystemLogs(limit: int = 100) -> list:
    # File path
    filePath = 'osiris-admin-portal/core-features/tests/logs/system.logs'  
    # Validate limit parameter
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    if limit < 0:
        raise ValueError("Limit cannot be negative.")
    logs = []
    if limit == 0:
        return logs
    try:
        with open(filePath, 'r') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                # Appends the log entry
                logs.append({
                    "event": row.get("event"),
                    "timestamp": row.get("timestamp"),
                    "service": row.get("service")
                })
                if index + 1 >= limit:  # Stop if the limit is reached
                    break
    except FileNotFoundError:
        print(f"Error: The file {filePath} was not found.")
        print()
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    return logs

# Example usage
while True:
    try:
        limit = int(input("Enter the number of logs to retrieve (or -1 to exit): "))
        if limit == -1:
            break  # Exit the loop if the user inputs -1
        logs = viewSystemLogs(limit=limit)
        # Check if logs are empty before printing
        if not logs:
            print("No logs found.")
        else:
            for log in logs:
                print(f"Event: {log['event']}, Timestamp: {log['timestamp']}, Service: {log['service']}")
    except ValueError as e:
        print(f"Error: {e}")

