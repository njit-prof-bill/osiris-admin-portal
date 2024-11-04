'''
Problem: Implement the addNewUser API, which adds a new user to the Osiris platform through the admin portal.

Type: Function

Function Signature:

def addNewUser(username: str, email: str, role: str) -> bool:
    pass
Description:

The addNewUser API allows an administrator to add a new user to the platform, specifying the username, email, and role (e.g., "admin", "developer", "viewer").
The function returns True if the user is successfully added, False otherwise.
Input:

username: The username for the new user. (string)
email: The email address of the new user. (string)
role: The role assigned to the new user (e.g., admin, developer, viewer). (string)
Output:

True if the user is successfully added, False otherwise.
Sample Input:

response = addNewUser("johndoe", "johndoe@example.com", "developer")
Sample Output:

response = True
'''
#this list will prob be factored out into a shared date file in src/
listOfUsers = []

test1 = {
    "username":"1n",
    "email":"danie@test.com",
    "role":"user"
}
test2 = {
    "username":"2n",
    "email":"d22222anie@test.com",
    "role":"user"
}
test3 = {
    "username":"3n",
    "email":"danid@test.com",
    "role":"usdddder"
}
listOfUsers.append(test1)
listOfUsers.append(test3)
listOfUsers.append(test2)

def updateUserRole(username: str, role: str) -> bool:

    if not username:
        print("no username give")
        return False
    if not role:
        print("no role given")
        return False

    global listOfUsers
    
    for user in listOfUsers:
        if username in user.values():
            user["role"] = role
            print("User Role Updated")
            return True
    
    print("User not found")
    return False


print(listOfUsers)
updateUserRole("2n","admin++++++++-------")
print(listOfUsers)

