def setSystemAlert(message: str, priority: str) -> bool:
    if priority != "low" and priority != "medium" and priority != "high":
        return False
    if len(message) == 0:
        return False
    else:
        return True

assert setSystemAlert("", "low") == False, "Test 1 failed"
assert setSystemAlert("", "urgent") == False, "Test 2 failed"
assert setSystemAlert("", "low") == False, "Test 3 failed"
assert setSystemAlert("System rebooted", "low") == True, "Test 4 failed"
assert setSystemAlert("Disk space low", "medium") == True, "Test 5 failed"
assert setSystemAlert("Critical error", "high") == True, "Test 6 failed"
assert setSystemAlert("System rebooted", "urgent") == False, "Test 7 failed"
assert setSystemAlert("System rebooted", "high-priority") == False, "Test 8 failed"

print("Tests passed")
