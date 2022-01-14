from Character import Character
from question import MultipleChoiceQuestion
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
        self.user.update_data_file()
        location_details ="You are outside the railway station, there is a three way road ahead, \nyou see a sign board infront of you, the sign board indicates that \nthere is an ancient temple of Lord Mudyuwana in the EAST direction, \nthere is the river Wamuduna in the WEST direction and \nthe Amudon Jungle towards the SOUTH direction \n In which direction would you like to proceed [N/W/E/S]?"
        call_meth = interaction(location_details, self.nowhere, self.temple, self.river, self.potion_seller)
        call_meth()
    
    def river(self):
        self.user.location = "river" 
        self.user.update_data_file()
        location_details = "You are standing near the beautiful Wamudana river nearby, but the entry is resticted beyond this,  In which direction do you want to proceed [N/E/W/S]?"
        call_meth = interaction(location_details, self.nowhere, self.beginning, self.nowhere, self.nowhere)
        call_meth()    
    
    def temple(self):
        self.user.location = "temple" 
        self.user.update_data_file()
        location_details = "You are standing near Lord Mudwana's temple, There is a beautiful river nearby, but the entry is resticted beyond this, In which direction do you want to proceed [N/E/W/S]?"
        call_meth = interaction(location_details, self.nowhere, self.nowhere, self.beginning, self.nowhere)
        call_meth()

    def nowhere(self):
        print("Sorry! you cannot go in this direction. Enter a different input")
        
        if(self.user.location=='beginning'):
            self.beginning()
        if(self.user.location=='temple'):
            self.temple()
        if(self.user.location=='river'):
            self.river()
        if(self.user.location=='potion_seller'):
            self.potion_seller()
        if(self.user.location=='Cognoblin'):
            self.cognoblin()
        

    def potion_seller(self):
        self.user.location = "potion_seller"
        self.user.update_data_file()
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
            self.user.update_data_file()
            print(f'You took the energy potion, Your energy is now {self.user.character.energy} and your current wealth is {self.user.character.wealth}')
        else:
            print("Sorry you don't have money to buy potion.")

    def cognoblin(self):
        self.user.location = "cognoblin"
        self.user.update_data_file()
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
            self.user.update_data_file()
            print("YOU WON THE GAME!!! YOU WON THE TREASURE OF WORTH 5000 BILLIO MUD POUNDS")
        else:
            print("YOU LOST THE GAME!!! THE GAME IS OVERRRRRRRRRR")

    def playQuestion(self):
        cognoblin_questions = ["Vincent has a paper route. Each morning, he delivers 37 newspapers to customers in his neighborhood. It takes Vincent 50 minutes to deliver all the papers. If Vincent is sick or has other plans, his friend Thomas, who lives on the same street, will sometimes deliver the papers for him.",
         "The Pacific yew is an evergreen tree that grows in the Pacific Northwest. The Pacific yew has a fleshy, poisonous fruit. Recently, taxol, a substance found in the bark of the Pacific yew, was discovered to be a promising new anticancer drug.",
         "Erin is twelve years old. For three years, she has been asking her parents for a dog. Her parents have told her that they believe a dog would not be happy in an apartment, but they have given her permission to have a bird. Erin has not yet decided what kind of bird she would like to have.",
         "Tim's commute never bothered him because there were always seats available on the train and he was able to spend his 40 minutes comfortably reading the newspaper or catching up on paperwork. Ever since the train schedule changed, the train has been extremely crowded, and by the time the doors open at his station, there isn't a seat to be found.",
         "When they heard news of the hurricane, Maya and Julian decided to change their vacation plans. Instead of traveling to the island beach resort, they booked a room at a fancy new spa in the mountains. Their plans were a bit more expensive, but they'd heard wonderful things about the spa and they were relieved to find availability on such short notice."]
        options_list =[["Vincent and Thomas live in the same neighborhood.","It takes Thomas more than 50 minutes to deliver the papers.","It is dark outside when Vincent begins his deliveries.","Thomas would like to have his own paper route."],
        ["Taxol is poisonous when taken by healthy people.","Taxol has cured people from various diseases.","People should not eat the fruit of the Pacific yew","The Pacific yew was considered worthless until taxol was discovered."],
        ["Erin's parents like birds better than they like dogs.","Erin does not like birds.","Erin and her parents live in an apartment.","Erin and her parents would like to move."],
        ["Tim would be better off taking the bus to work.","Tim's commute is less comfortable since the train schedule changed.","Many commuters will complain about the new train schedule.","Tim will likely look for a new job closer to home."],
        ["Maya and Julian take beach vacations every year.","The spa is overpriced.","It is usually necessary to book at least six months in advance at the spa.","Maya and Julian decided to change their vacation plans because of the hurricane."]]
        answers_list = [1, 3, 3, 2, 4]
        mcq = MultipleChoiceQuestion(cognoblin_questions, answers_list, options_list)
        que_dict = mcq.generateQuestion()
        print(que_dict.get('query'))
        print(f'1. {que_dict.get("option_0")} \n2. {que_dict.get("option_1")} \n3. {que_dict.get("option_2")} \n4. {que_dict.get("option_3")}')
        user_answer= input('Please choose the correct option to proceed [1/2/3/4]: ')  
        if mcq.matchAnswer(que_dict.get('query'), user_answer) == True:
            won = True
            print("You were able to answer the question Correctly, Cognoblin opens the door of treasure for you!!!")
        else:
            won = False
            print("You answered the question Incorrectly, Cognoblin is angry now. He is Going to kill You!!!")
        return won

    def payCognoblin(self):
        if self.user.character.wealth > 1000:
            print("You were able to pay Cognoblin 1000 Gold Coins so he unlocks the door to treasure for you!!!")
            won = True
        else:
            print("You don't have 1000 Gold Coins, you are unable to pay Cognoblin 1000 Gold Coins, He is angry now!!!")
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
       

    def help(self):
        print("MUD-MASH is a text based game, You can use the following text commands to proceed in the game.")
        print("\nLocation -- Use this command to get details about the location")
        print("L -- Use this command to get details about the location")
        print("Go North -- Use this command to move towards north direction")
        print("GN -- Use this command to move towards north direction")
        print("Go South -- Use this command to move towards south direction")
        print("GS -- Use this command to move towards south direction")
        print("Go East -- Use this command to move towards East direction")
        print("GE -- Use this command to move towards East direction")
        print("Go West -- Use this command to move towards West direction")
        print("GW -- Use this command to move towards West direction")
        print("Quit -- Use this command to quit the game.")
        print("Q-- Use this command to quit the game.")

        if(self.user.location=='beginning'):
            self.beginning()
        if(self.user.location=='temple'):
            self.temple()
        if(self.user.location=='river'):
            self.river()
        if(self.user.location=='potion_seller'):
            self.potion_seller()
        if(self.user.location=='Cognoblin'):
            self.cognoblin()