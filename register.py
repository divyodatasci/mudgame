from getpass import getpass
from user import User
from login import *

#function for registering new user
def register_user():
    print("Enter details to register.")
    flag1 = False                               #flag1 becomes true when username gets accepted
    while flag1 == False:
        username = input("Please enter an username: ")  #username input is taken
        usernames_file = open('usernames.txt', 'r')     #username.txt is opened to check if 
        lines = usernames_file.readlines()              #username is already present in the file
        usernames_file.close()                        
        if len(lines) == 0:
            break
        for line in lines:
            if username+"\n" == line:
                flag1 = False
                print("username already present, please enter a new username")
                break
            else:
                flag1= True
        

    flag2 = False                   #flag2 becomes true when registration gets completed
    while flag2 == False:
        password = getpass("Please enter a password: ")    #taking the password input
        repassword = getpass("Please re-enter password: ")
        if password == repassword:                          #checking if both the passwords match
            usernames_file = open('usernames.txt', 'a')     #usernames.txt keeps all the usernames
            user_file = open('users.txt', 'a')              #users.txt keeps the information of the user and last game
            usernames_file.write(username+"\n")             #saving username in usernames.txt
            usernames_file.close()
            user = User(username, password)
            user_file.write(f'{username},{password},null,null,{0},{0},{0},null')  #saving user info
            user_file.close()
            print("Registration Successful, You can proceed with the game.")
            flag2 = True
        else:
            print("Sorry! Password Did not match")
    return user
