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

def addNewUser(username: str, email: str, role: str) -> bool:

    if not username:
        return False
    if not email:
        return False
    if not role:
        return False

    global listOfUsers
    userToAdd = {
        username,
        email,
        role
    }
    listOfUsers.append(userToAdd)
    return True


addNewUser("1n","danie@test.com","user")
addNewUser("n","d22222anie@test.com","user")
addNewUser("n","danie@test.com","usdddder")
print(listOfUsers[2])