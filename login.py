from getpass import getpass
from Character import Character
from user import   User


# function for logging in user
def login_user(username, password):
    user_file = open('users.txt','r')          # users.txt has all the user details
    lines = user_file.readlines()               
    player=""
    if len(lines) > 0:
        for line in lines: 
            line_data = line.split(',')
            id=str(line_data[0])
            pw=str(line_data[1])
            if (id == str(username)) and (pw==str(password)) :                            # authenticating by checking user information
                
                name= str(line_data[2])
                sex=str(line_data[3])
                energy=int(line_data[4])
                fighting_skill=int(line_data[5])
                wealth=int(line_data[6]) 
                location = str(line_data[7].strip())
                player = User(username, password, name, sex, energy, fighting_skill, wealth, location )   # creating user object 
                break
    return player    
        
 