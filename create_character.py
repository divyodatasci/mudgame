from begin_game import *
def create_character():
    major_attributes = ["Rich","Fighter", "Strong"]
    fname = input('Please tell us your desired first name for the game: ')
    flag= False
    while (flag == False):
        if(fname.isalpha()):
            flag= True
        else:
            print("Sorry! We cannot process the name you entered. Your first name should contain only alphabets.")
            fname = input('Please enter a desired first name for the game: ')
    flag= False
    lname = input('Please tell us your desired last name for the game: ')
    while (flag == False):
        if(lname.isalpha()):
            flag= True
        else:
            print("Sorry! We cannot process the input you entered for last name. \nYour last name should contain only alphabets.")
            lname = input('Please enter a desired last name for the game: ')
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
    print('\nThere are three major attributes to choose from, Each attribute has its own benifit \n 1. Rich - if you choose Rich you get 1000 Gold coins, you can use them in the game in various stages \n 2. Strong- If you choose to be strong, you get 1000 MegaCalories of energy, you will need energy in various stages. \n 3. Fighter- If you choose to be a fighter, you get 1000 fighting skill points, you can use fighting skills to fight with monsters and people in the game.')
    attribute_selected = int(input("Please choose an option from above. Please enter a number corresponding to the attribute 1/2/3: "))
    player = {
        "name": fname+" "+lname,
        "sex": sex,
        "gold_coins": 200,
        "energy": 200,
        "fighting_skill": 200
    }

    if attribute_selected == 1:
        player["gold_coins"] = 1000
    elif attribute_selected == 2:
        player["energy"] = 1000
    else :
        player["fighting_skill"] = 1000

    print(f"\n\n\nHi {fname}!, You are ready for the game, Following are your details:")
    #print(player.get('gold_coins'))

    print(f'Name: {player["name"]} \t Sex: {player["sex"]} \nGold Coins: {player["gold_coins"]}  \t Energy: {player["energy"]} MegaCalories  \t Fighting Skills : {player["fighting_skill"]} Fighting Skill Points ')