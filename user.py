from Character import Character


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.character = ""
        self.score = 0
        self.level=0

    def create_character(self):
        flag= False
        while (flag == False):
            name = input('Please tell us your desired name for the game: ')
            if(name.isalpha()):
                flag= True
            else:
                print("Sorry! We cannot process the name you entered. Your first name should contain only alphabets.")
          
        sex = str(input('\nPlease mention your gender Male/Female/Others: '))
        flag = False
        while(flag== False):
            if(sex.title() =='Male' or sex.title() == 'M'):
                sex = 'Male'
                flag = True
            elif(sex.title() == 'Female' or sex.title() == 'F'):
                sex = 'Female' 
                flag = True  
            elif(sex.title() == 'Others' or sex.title() =='Other' or sex.title() == 'None' or sex.title() == 'No'):
                sex = 'Others'
                flag = True
            else:
                print('\nSorry, we are unable to process your input.')
                sex = input('\nPlease mention one from Male/Female/Others: ')
        print("\n \nChoose an Attribute -----------------------------------------------------------------------------")
        print('\nThere are three major class to choose from, Each class has its own benifit \n 1. RichYanki  \n 2. Strongrogdor \n 3. Fighterelf')
        attribute_selected = int(input("Please choose an option from above. Please enter a number corresponding to the attribute 1/2/3: "))
        
        if attribute_selected == 1 or str(attribute_selected).lower() == 'richyanki':
            gold_coins = 1000
            energy = 300
            fighting_skill = 100
        elif attribute_selected == 2 or str(attribute_selected).title() == 'Strongrogdor':
            energy = 1100
            fighting_skill = 200
            gold_coins = 100
        elif attribute_selected == 3 or str(attribute_selected).title() == 'Fighterelf' :
            fighting_skill = 800
            energy = 500
            gold_coins = 100


        player = Character(name.title(),sex,energy,fighting_skill, gold_coins)
        self.character=player
        print(f"\n\n\nHi {player.name}!, You are ready for the game, Following are your details:")
        
        print(f'Name: {player.name} \t Sex: {player.sex} \nGold Coins: {player.wealth}  \t Energy: {player.energy} MegaCalories  \t Fighting Skills : {player.fighting_skill} Fighting Skill Points ')
        
#create_character()

'''class LoggedInUser(User):
    def __init__(self, username, password):
        super().__init__(username,password)
        self.character = ""
        self.score = 0
        self.level=0'''
