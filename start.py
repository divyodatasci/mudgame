from register import *
from login import *
from utility import *

# This is the main method, the game starts from this method, this is the first method
#  which is called on the run of this appliication
def main():
    flag = False   # flag becomes true once the user is able to login
    user=''
    while flag == False:
        if askYesOrNo("Are you a registered user [Y/N]?"):
            print("Enter your login details.")  
            username= input("Enter your username: ")  
            password= getpass("Enter your password: ")    # askYesOrNo function is called 
            user=login_user(username, password)     # calls login function if answer is yes
        else:
            print("Enter details to register.")
            flag1 = False  
            while flag1 == False:
                username = input("Please enter an username: ")  
                usernames_file = open('usernames.txt', 'r')     # username.txt is opened to check if 
                lines = usernames_file.readlines()              # username is already present in the file
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
                if password == repassword:
                    user=register_user(username, password)  # calls register function if answer is no
                    flag2 = True
                else:
                    print("Sorry! Password Did not match")
        if user != "":
            flag = True
        else:
            print("Sorry! Either the username or password is wrong, Please register or login again.")
    print(f'Hi {user.username}, You have Successfully Logged-in into the game.')

    flag_character_creation = False
    
    if (user.character.name == 'null' and user.location != 'won'):

        while flag_character_creation == False:
            user.create_character()
            if askYesOrNo("Are you okay with the created character for your game [Y/N]?"):   # askYesOrNo function is called 
                flag_character_creation = True
                print()
                print()
                print()
    user.play_game()     # This begins the game for the created character
                    




if __name__ == "__main__":
    main()