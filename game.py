from Character import Character
from utility import *
import time 
# Following class has all the methods related to the game, sets the reponse of the game on input of the player
class Game:
    def __init__(self, user):
        self.name = "MUDMASH"
        self.user= user
    def showGameMap(self):
        print("                         Railway Station")
        print()
        print(" Wamudana River =============         ======================= Mudwana Temple")
        print("                                ||")
        print("                                ||")
        print("                                ||")
        print("                                ||")
        print("------------------- A M U D O N     F O R E S T ------------------------------")
        print("                                ||")
        print("                              Potion Seller  ====== Cognoblin ===== Treasure")
        print()


    def beginning(self):
        self.user.location = "beginning"
        print(self.user.username)
        print(self.user.password)
        print(self.user.character.name)
        print(self.user.character.sex)
        print(self.user.character.wealth)
        # print(self.user.character.)
        # print(self.user.password)
        # print(self.user.username)
        # print(self.user.password)
        # character
        location_details ="You are outside the railway station, there is a three way road ahead, you see a sign board infront of you, the sign board indicates that \nthere is an ancient temple of Lord Mudyuwana in the EAST direction, \nthere is the river Wamuduna in the WEST direction and \nthe Amudon Jungle towards the SOUTH direction \n In which direction would you like to proceed [N/W/E/S]?"
        call_meth = interaction(location_details, self.nowhere, self.temple, self.nowhere, self.potion_seller)
        call_meth()
    
    

    
     
    # def actionOnInput(self, input_command, location, north, east, west, south):
        
        
    
    def temple(self):
        self.user.location = "temple" 
        print("You are standing near Lord Mudwana's temple, There is a beautiful river nearby, but the entry is resticted beyond this, In which direction do you want to proceed [N/E/W/S]?")
        
    def nowhere(self):
        print("Sorry! you cannot go in this direction. Enter a different input")
        if(self.user.location=='beginning'):
            self.beginning()
        if(self.user.location=='potion_seller'):
            self.potion_seller()
        if(self.user.location=='Cognoblin'):
            self.cognoblin()
        

    def potion_seller(self):
        self.user.location = "potion_seller"
        location_details ="You are in the Amudon Jungle, there is a cave in the EAST Direction, you need to go through that cave to reach the treasure. \n In which direction would you like to proceed [N/W/E/S]?"
        
        print("You reach half way towards jungle, you see there are no entry sign boards in both SOUTH and WEST direction, You see a man selling energy potion. \nThe man tells you that if you drink the energy potion, you gain 1500 MegaCalories of energy from the potion but you need to pay 500 Gold Coins for the potion.")
        
        if askYesOrNo("Would you like to buy and drink the potion [Y/N]?"):
            self.buy_potion()
            call_meth=interaction(location_details, self.beginning, self.cognoblin, self.nowhere, self.nowhere)
            call_meth()
        else:
            self.cognoblin()
    def buy_potion(self):
        if(self.user.character.wealth >= 500):
            self.user.character.wealth = self.user.character.wealth - 500
            self.user.character.energy = self.user.character.energy + 1500
            print(f'You took the energy potion, Your energy is now {self.user.character.energy} and your current wealth is {self.user.character.wealth}')
        else:
            print("Sorry you don't have money to buy potion.")

    def cognoblin(self):
        self.user.location = "cognoblin"
        print()
        print()
        print("You have entered a cave made of hard rocks, Lights are flashing all around, It is impossible to move in any of the direction because all the ways out of the cave are locked. Infront of you stands a BIG MONSTER named Cognoblin.")
        print('Cognoblin is very strong and powerful monster, He has the best fighting skills in Amudon Jungle.')
        print('He is a very intelligent monster and he likes people who are intelligent.')
        print('But, he is bit greedy, if someone gives him the gold coins he asks for, he leaves them and unlocks the door to treasure.')
        print(f'Cognoblin says, "Hello{"Player"}, Welcome to the land of treasure, I will only allow you to move ahead')
        print('1. If you answer my question correctly')
        print('2. If you pay me 1000 Gold Coins ')
        print('3. If you win in a fight with me "') 
        print('"I will kill you if you choose an option and are unable to succeed in that task')
        print("How do you want to proceed?")

        user_input = int(input("Please provide your choice [1/2/3]: "))
        win = False
        if user_input == 1:
            win = self.playQuestion()
        elif user_input == 2:
            win = self.payCognoblin()
        elif user_input == 3:
            win = self.fightCognoblin()
        else:
            print("Sorry, that was an invalid input")
            self.cognoblin()
        if win == True:
            self.user.location = 'won'
    def playQuestion():
        print       
    def payCognoblin(self):
        if self.user.character.wealth > 1000:
            print("You were able to pay Cognoblin 1000 Gold Coins so he unlocks the door to treasure for you")
            won = True
        else:
            print("You don't have 1000 Gold Coins, you are unable to pay Cognoblin 1000 Gold Coins, He is angry now.")
            won = False
        return won 
    
    def fightCognoblin(self):
        cognoblin =  Character('Cognoblin','O','1000','150','15000')
        player = self.user.character
        while int(player.energy) >= 0 and int(cognoblin.energy) > 0:
            time.sleep(.75)
            print('You attacked Cognoblin')
            player.energy = player.energy - 40
            cognoblin.energy = int(cognoblin.energy) - 3 * int(player.fighting_skill)
            time.sleep(.75)
            print (f'You lost 40 Mega Calories and Cognoblin lost {3 * int(player.fighting_skill)} Mega Calories')
            time.sleep(.75)
            print('Cognoblin attacked you')
            cognoblin.energy = cognoblin.energy - 40
            player.energy = int(player.energy) - 3 * int(cognoblin.fighting_skill)
            time.sleep(.75)
            print (f'Cognoblin lost 40 Mega Calories and you lost {3 * int(cognoblin.fighting_skill)} Mega Calories')
            
        won = False
        if player.energy > cognoblin.energy:
            won=True
            print("Cognoblin has no more energy to fight. You were able to beat Cognoblin in the fight, You have won the fight")
        else:
            print("You have no more energy to fight, Sorry You lost the match")

        return won
       

    
