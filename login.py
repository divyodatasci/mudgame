from getpass import getpass
from user import   User


# function for logging in user
def login_user():
    print("Enter your login details.")  
    username= input("Enter your username: ")  # username input
    password= getpass("Enter your password: ") # password input
    user_file = open('users.txt','r')          # users.txt has all the user details
    lines = user_file.readlines()               # storing all the lines of users.txt file in lines
    player=""
    for line in lines:                                  # loop for reading and checking each line
        if line == "username:"+username + " password:"+ password+"\n":
            player = User(username, password)                            # authenticating by checking user information
            break
    return player    
        
       
    
# following method is used to authenticate the details
def authenticate(id, password):
    user_file = open('users.txt','r')
    lines = user_file.readlines()
    for line in lines:
        if line == "username:"+id + " password:"+ password+"\n":

            return True
    return False