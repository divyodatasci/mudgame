from getpass import getpass
from create_character import *



def login():
    flag_login= False
    while flag_login == False:
        username= input("Enter your username: ")
        password= getpass("Enter your password: ")
        if authenticate(username, password ) == True:
            print("You have logged in to the game successfully")
            flag_login = True
        else:
            print("Either the username or password is wrong, Please re-enter your login details.")

    print("Choose one of the option from the below menu \n1. Enter 1 to  Play Game \n2. Enter 2 to Check Scores ")
    choice_flag = False
    while(choice_flag == False):
        choice = int(input("Enter your choice from the above menu: "))
        if choice == 1:
            choice_flag= True
            create_character()
        elif choice == 2:
            choice_flag=True
            check_scores()
        else:
            print("It was an invalid choice, Please choose from the below menu \n1. Enter 1 to  Play Game \n2. Enter 2 to Check Scores ")
        

def authenticate(id, password):
    user_file = open('users.txt','r')
    lines = user_file.readlines()
    for line in lines:
        if line == "username:"+id + " password:"+ password+"\n":
            return True
    return False