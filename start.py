from register import *
from login import *
from utility import *

def main():
    flag = False   # flag becomes true once the user is able to login
    player=''
    while flag == False:
        if askYesOrNo("Are you an registered user [Y/N]?"):   # askYesOrNo function is called 
            player=login_user()     # calls login function if answer is yes
        else:
            player=register_user()  # calls register function if answer is no
        if player != "":
            flag = True
        else:
            print("Sorry! Either the username or password is wrong, Please register or login again.")
    print(player)

    flag_character_creation = False
    
    if (player.character.name == 'null' and player.location != 'won'):

        while flag_character_creation == False:
            player.create_character()
            if askYesOrNo("Are you okay with the created character for your game [Y/N]?"):   # askYesOrNo function is called 
                flag_character_creation = True
                print()
                print()
                print()
    player.play_game()     # This begins the game for the created character
                    


# general function for asking yes/no question
# the input parameter for this function is the question to be asked


if __name__ == "__main__":
    main()