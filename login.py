from getpass import getpass
from create_character import *
from user import   User



def login_user():
    print("Enter your login details.")
    username= input("Enter your username: ")
    password= getpass("Enter your password: ")
    user_file = open('users.txt','r')
    lines = user_file.readlines()
    player=""
    for line in lines:
        if line == "username:"+username + " password:"+ password+"\n":
            player = User(username, password)
            break
    return player    
        
       
    

def authenticate(id, password):
    user_file = open('users.txt','r')
    lines = user_file.readlines()
    for line in lines:
        if line == "username:"+id + " password:"+ password+"\n":

            return True
    return False