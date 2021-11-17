from getpass import getpass

from login import login
from register import register_user

def fetch_user_details():
    username = input("Please enter username: ") 
    usernames_file = open('usernames.txt', 'r')     #
    lines = usernames_file.readlines()              #
    usernames_file.close()                        
    if len(lines) == 0:
        register_user(username)
    else:
         if username+"\n" in lines:
             login_user(username)
         else:
             print(f'{username} does not exist')
             input_accepted = False
             while input_accepted == False:
                new_user = input("Do you want to create a new account Y/n? ")
                if new_user.title() == 'Y' or new_user.title() == 'Yes':
                    input_accepted = True
                    register_user(username)
                elif new_user.title() == 'N' or new_user.title() == 'No':
                    input_accepted = True
                    fetch_user_details()
                else:
                    print("Please provide a valid input")




def register_user(username):
    password_flag = False
    while password_flag == False:
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
            password_flag = True
        else:
            print("Sorry! Password Did not match")

    print("User registered Successfully")

def login_user(username):
    print("User Logged In Successfully")