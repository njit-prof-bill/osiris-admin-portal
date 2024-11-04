import pytest

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


service_states = {
    "auth": "stopped",
    "database": "stopped",
    "message_queue": "stopped"
}

@pytest.fixture(autouse=True)
def reset_service_states():
    global service_states
    service_states = {
        "auth": "stopped",
        "database": "stopped",
        "message_queue": "stopped"
    }

def test_start_service():
    assert manageService("auth", "start") is True
    assert service_states["auth"] == "running"

    assert manageService("database", "start") is True
    assert service_states["database"] == "running"

def test_start_already_running_service():
    service_states["auth"] = "running"
    assert manageService("auth", "start") is False
    assert service_states["auth"] == "running"

def test_stop_service():
    service_states["auth"] = "running"
    assert manageService("auth", "stop") is True
    assert service_states["auth"] == "stopped"

    service_states["message_queue"] = "running"
    assert manageService("message_queue", "stop") is True
    assert service_states["message_queue"] == "stopped"

def test_stop_already_stopped_service():
    assert manageService("auth", "stop") is False
    assert service_states["auth"] == "stopped"

def test_restart_service():
    service_states["auth"] = "stopped"
    assert manageService("auth", "restart") is True
    assert service_states["auth"] == "running"

def test_invalid_service_name():
    assert manageService("non_existent_service", "start") is False

def test_invalid_action():
    assert manageService("auth", "pause") is False
