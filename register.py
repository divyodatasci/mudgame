from getpass import getpass
from user import User
from login import *


def register_user(username, password):
    user="" 
    usernames_file = open('usernames.txt', 'a')     #usernames.txt keeps all the usernames
    user_file = open('users.txt', 'a')              #users.txt keeps the information of the user and last game
    usernames_file.write(username+"\n")             #saving username in usernames.txt
    usernames_file.close()
    user = User(username, password, 'null' , 'null', 0, 0, 0, 'null')
    user_file.write(f'{username},{password},null,null,{0},{0},{0},null'+'\n')  #saving user info
    user_file.close()
    print("Registration Successful, You can proceed with the game.")
           
    return user
