from getpass import getpass
from login import *

#function for registering new user
def register_user():
    flag1 = False
    while flag1 == False:
        username = input("Please enter an username: ")  #
        usernames_file = open('usernames.txt', 'r')     #
        lines = usernames_file.readlines()              #
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
        

    flag2 = False
    while flag2 == False:
        password = getpass("Please enter a password: ")
        repassword = getpass("Please re-enter password: ")
        if password == repassword:
            usernames_file = open('usernames.txt', 'a')
            user_file = open('users.txt', 'a')
            usernames_file.write(username+"\n")
            usernames_file.close()
            user_file.write("username:"+username + " password:"+ password+"\n")
            user_file.close()
            print("Registration Successful, You can proceed with login and play the game.")
            flag2 = True
        else:
            print("Sorry! Password Did not match")

    login()
