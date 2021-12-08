from getpass import getpass
from Character import Character
from user import   User


# function for logging in user
def login_user():
    print("Enter your login details.")  
    username= input("Enter your username: ")  # username input
    password= getpass("Enter your password: ") # password input
    user_file = open('users.txt','r')          # users.txt has all the user details
    lines = user_file.readlines()               # storing all the lines of users.txt file in lines
    player=""
    if len(lines) > 0:
        for line in lines: 
            line_data = line.split(',')
            id=str(line_data[0])
            pw=str(line_data[1])
            if (id == str(username)) and (pw==str(password)) :                            # authenticating by checking user information
                player = User(username, password)   # creating user object 
                name= str(line_data[2])
                sex=str(line_data[3])
                energy=int(line_data[4])
                fighting_skill=int(line_data[5])
                wealth=int(line_data[6]) 
                character = Character(name, sex, energy, fighting_skill, wealth)
                player.character = character
                player.location = str(line_data[7])
                break
    return player    
        
       
    
# following method is used to authenticate the details
def authenticate(id, password):
    user_file = open('users.txt','r')
    lines = user_file.readlines()
    for line in lines:
        line_data = line.split(',')
        if line_data[0] == id & line_data[1]==password :

            return True
    return False