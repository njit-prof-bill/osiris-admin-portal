import csv
import logging
from ast import literal_eval

# Configure logging for configuration changes
logging.basicConfig(
    filename="osiris-admin-portal/core-features/tests/logs/configChanges.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Load configuration settings from the CSV file
def loadConfig(filename="osiris-admin-portal/core-features/tests/configSettings/configSet.csv"):
    confSett = {}
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row["setting"]
                # Convert value types based on stored type 
                try:
                    confSett[key] = literal_eval(row["value"])
                except (ValueError, SyntaxError):
                    confSett[key] = row["value"]
    except FileNotFoundError:
        logging.error("Configuration file not found.")
    return confSett

# Save configuration settings back to the CSV file
def saveConfig(configuration, filename="osiris-admin-portal/core-features/tests/configSettings/configSet.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["setting", "value"])
            for key, value in configuration.items():
                writer.writerow([key, repr(value)])
    except Exception as e:
        logging.error(f"Failed to save configuration: {e}")

def updateSystemConfiguration(setting: str, value: any) -> bool:
    # Load the initial configuration
    configSet = loadConfig()
    
    # Check if the setting exists
    if setting in configSet:
        try:
            # Log the current and new value
            oldValue = configSet[setting]
                
            # Update the configuration setting
            configSet[setting] = value
                
            # Save updated configuration to file
            saveConfig(configSet)
                
            # Log change
            logging.info(f"Updated '{setting}' from '{oldValue}' to '{value}'")
                
            return True
        except Exception as e:
            logging.error(f"Error updating setting {setting}: {e}")
            return False
    else:
        # If the setting does not exist
        print(f"Setting '{setting}' not found.")
        return False

# Sample usage
response = updateSystemConfiguration("maintenance_mode",False)
print(response)  # Expected output: True
