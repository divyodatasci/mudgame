# Following method works as a general method for responding to user input
# The input parameters for the below method are thename of the methods to be
#  called on different user input 

def interaction(location_details, north, east, west, south):
        print(location_details)
        flag_dir = False  # flag becomes true if user provides correct input value
        return_meth = ""
        while flag_dir == False:
            input_command = input("Enter an input to proceed: ")
            if input_command.title() == 'Location' or input_command.title() == 'L':
                print(location_details)
                
            elif input_command.title() in ['Go North','Gn', 'North', 'N']:
                flag_dir= True
                return_meth = north

            elif input_command.title() in ['Go East' , 'Ge', 'East', 'E']:
                flag_dir= True
                return_meth = east
                
            elif input_command.title() in ['Go West', 'Gw', 'West', 'W']:
                flag_dir= True
                return_meth = west
            elif input_command.title() in ['Go South', 'Gs', 'South', 'S']:
                flag_dir= True
                return_meth = south
            else:
                print("This input is invalid in this stage, please provide a different input")
            
        return return_meth        
def askYesOrNo(question):
    flag = False     # flag becomes true once the user gives a valid answer
    while flag==False:
        answer = input(question+": ")
        if answer.title() in ["Yes", "Y"]:
            flag = True
            return True
        elif answer.title() in ["No", "N"]:
            flag = True
            return False
        else:
            print("Sorry! your answer was invalid, please enter your answer again.")
