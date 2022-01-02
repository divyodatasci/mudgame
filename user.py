from Character import Character
from game import Game

# following class stores the player information and also performs the actions of player
class User:
    def __init__(self, username, password, name, sex,  energy, fighting_skill, wealth, location):
        self.username = username
        self.password = password
        self.character = Character(name, sex, energy, fighting_skill, wealth)
        self.location= location

    # following method is used for creating character 
    def create_character(self):
        flag_name= False   # flag_name becomes true when user provides only alphabets
        while (flag_name == False):
            name = input('Please tell us your desired name for the game: ')  # input for character name 
            if(name.isalpha()):
                flag_name= True
            else:
                print("Sorry! We cannot process the name you entered. Your first name should contain only alphabets.")
          
        sex = str(input('\nPlease mention your gender Male/Female/Others [M/F/O]: '))   # input for character's gender
        flag_gender = False  # flag_name becomes true when user provides correct gender input
        while(flag_gender== False):
            if(sex.title() =='Male' or sex.title() == 'M'):
                sex = 'Male'
                flag_gender = True
            elif(sex.title() == 'Female' or sex.title() == 'F'):
                sex = 'Female' 
                flag_gender = True  
            elif(sex.title() == 'Others' or sex.title() =='O' or sex.title() == 'None' or sex.title() == 'No'):
                sex = 'Others'
                flag_gender = True
            else:
                print('\nSorry, we are unable to process your input.')
                sex = input('\nPlease mention one from Male/Female/Others [M/F/O]: ')


        print("\n \nChoose an Attribute -----------------------------------------------------------------------------")
        print('\nThere are three major class to choose from, Each class has its own benifit')
        print('\n 1. RichYanki  \n 2. Strongrogdor \n 3. Fighterelf') # Name of different classes
        
        flag_attribute = False

        while flag_attribute == False:
            # input for class selection
            attribute_selected = int(input("Please choose an option from above. Please enter a number corresponding to the attribute 1/2/3: "))
            
            if attribute_selected == 1 or str(attribute_selected).lower() == 'richyanki':
                gold_coins = 1000  # setting attributes' values according to selected class
                energy = 300
                fighting_skill = 100
                flag_attribute = True
            elif attribute_selected == 2 or str(attribute_selected).title() == 'Strongrogdor':
                energy = 1100       # setting attributes' values according to selected class
                fighting_skill = 200
                gold_coins = 100
                flag_attribute = True
            elif attribute_selected == 3 or str(attribute_selected).title() == 'Fighterelf' :
                fighting_skill = 800   # setting attributes' values according to selected class
                energy = 500
                gold_coins = 100
                flag_attribute = True
            else:
                print("Sorry, that was an invalid input")


        player = Character(name.title(),sex,energy,fighting_skill, gold_coins) # Character object is created
        self.character=player       # setting character object as an attribute value to the user object
        print(f"\n\n\nHi {player.name}!, You are ready for the game, Following are your details:")
        
        print(f'Name: {player.name} \t Sex: {player.sex} \nGold Coins: {player.wealth}  \t Energy: {player.energy} MegaCalories  \t Fighting Skills : {player.fighting_skill} Fighting Skill Points ')
        
        

    # This method is used to start the game for the user
    def play_game(self):
        game = Game(self)  # Creating an object of Game class
        game.showGameMap()
        if(self.location=='null' or 'beginning'): 
            game.beginning() # Calling the beginning method of game class
        elif(self.location=='potion_seller'):
            game.potion_seller()
        elif(self.location=='cognoblin'):
            game.cognoblin()


    def update_data_file(self):
        user_file = open('users.txt','r')          # users.txt has all the user details
        lines = user_file.readlines()               # storing all the lines of users.txt file in lines
        
        if len(lines) > 0:
            i=0
            for line in lines: 
                line_data = line.split(',')
                id=str(line_data[0])
                if id == str(self.username):     # authenticating by checking user information
                    lines[i] = f'{self.username},{self.password},{self.character.name},{self.character.sex},{self.character.energy},{self.character.fighting_skill},{self.character.wealth},{self.location}'+'\n'
                    break
                i = i+1
        
        user_file.close()
        user_file = open('users.txt','w')  
        for line in lines:
            user_file.write(line)