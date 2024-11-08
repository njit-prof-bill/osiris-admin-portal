def generateUsageReport(timeframe: str) -> dict:
    data = {
        "daily": {
            "active_users": 50,
            "cpu_usage": "20%",
            "memory_usage": "30%",
            "total_transactions": 100
        },
        "weekly": {
            "active_users": 120,
            "cpu_usage": "50%",
            "memory_usage": "65%",
            "total_transactions": 320
        },
        "monthly": {
            "active_users": 500,
            "cpu_usage": "70%",
            "memory_usage": "80%",
            "total_transactions": 1300
        }
    }
    
    if timeframe in data:
        return data[timeframe]
    else:
        raise ValueError("Invalid timeframe. Please specify 'daily', 'weekly', or 'monthly'.")

# Example usage
report = generateUsageReport("weekly")
print(report)
