def beginning():
    print("You are outside the railway station, you see a sign board infront of you, the sign board indicates that \nthere is an ancient temple of Lord Mudyuwana in the EAST direction, \nthere is the river Wamuduna in the WEST direction and \nthe Amudon Jungle towards the NORTH direction")
    
    flag_dir = False
    while flag_dir == False:
        input_command = input()
        if input_command.title() == 'Location' or input_command.title() == 'L':
            flag_dir=True
            beginning()
        elif input_command.title() in ['Go North','Gn', 'North', 'N']:
            flag_dir=True
            potion_seller()
        elif input_command.title() in ['Go East' , 'Ge', 'East', 'E']:
            flag_dir=True
            goEast()
        elif input_command.title() in ['Go West', 'Gw', 'West', 'W']:
            flag_dir=True
            goWest()
        elif input_command.title() in ['Go South', 'Gs', 'South', 'S']:
            print("You cannot move in this direction, please provide a different input")
        elif 'Fight' in input_command.title():
            print("There is nothing to fight with here, please provide a different input")
        elif 'Break' in input_command.title():
            print("There is nothing to break here, please provide a different input")
        elif input_command.title() == 'Inventory' or input_command.title() == 'I':
            flag_dir=True
            inventory("beginning")
        elif input_command.title() == 'Help' or input_command.title() == 'H':
            help("beginning")
        else:
             print("This input is invalid in this stage, please provide a different input")
           
def goEast():
    print("Reached buy_potion")

def goWest():
    print("Reached buy_potion")

def buy_potion():
    print("Reached buy_potion")

def inventory(position):
    print("Reached buy_potion")

def potion_seller():
    print("You reach half way towards jungle, you see there are no entry sign boards in both east and west direction, You see a man selling energy potion. \nThe man tells you that if you drink the energy potion, you gain 1000 MegaCalories of energy from the potion but you need to pay 500 Gold Coins for the potion.")
    drink_potion = input("Would you like to buy and drink the potion Y/n?")
    if drink_potion.title() in ["Yes","Y"]:
        buy_potion()
        skill_teacher()
    elif drink_potion in ["No","n", "no"]:
        skill_teacher()
def buy_potion():
    print("Reached buy_potion")



def skill_teacher():
    print("You see a banner which says 'Pay and learn Fighting Centre', The centre teaches you fighting which increases your fighting skill by 1000 fighting skill points, You need to pay 300 gold coins to learn fighting.")
    learn_fighting = input("Would you like to pay and learn fighting Y/n?")
    if learn_fighting.title() in ["Yes","Y"]: 
        pay_for_fighting()
        cognoblin()
    elif learn_fighting in ["No", "no", "n"]:
        cognoblin()

def pay_for_fighting():
    print("Reached pay_for_fighting")


def cognoblin():
    print("You have entered a jungle with Trees and Bushes all around, It is impossible to move in any of the direction because of the bushes and trees. Infront of you stands a BIG MONSTER named Cognoblin.")
    print('Cognoblin is very strong and powerful monster, He has the best fighting skills in Amudon Jungle.')
    print('He is a very intelligent monster and he likes only those people who are intelligent.')
    print(f'Cognoblin says, "Hello{"Player"}, Welcome to the land of treasure, I will only allow you to move ahead, if you answer my question correctly". He then asks you to solve the following puzzle ') 
    print("Question")
    answer = input("Enter the correct answer")
    if answer.title() in ["Go North", "North", "N", "Gn", "Go East", "East", "Ge", "E", "Go West", "West", "Gw", "W" ]:
        print("Sorry! You cannot move in this direction.")
    if answer.title() in ["Go South", "South", "S", "Gs"]:
        skill_teacher()
    if answer.isdigit():
        print("Match Answer")
    if "Fight" in answer.title():
        if answer.title() == "Fight":
            print("Whom do you want to fight with, please enter the command [FIGHT {element name}] ")
        elif answer.title() in ["Fight Cognoblin", "Fight Monster"]:
            print("Fight Monster")
#beginning()