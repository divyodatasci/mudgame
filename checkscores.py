'''print("Choose one of the option from the below menu \n1. Enter 1 to  Play Game \n2. Enter 2 to Check Scores ")
    choice_flag = False
    while(choice_flag == False):
        choice = int(input("Enter your choice from the above menu: "))
        if choice == 1:
            choice_flag= True
            create_character()
        elif choice == 2:
            choice_flag=True
            check_scores()
        else:
            print("It was an invalid choice, Please choose from the below menu \n1. Enter 1 to  Play Game \n2. Enter 2 to Check Scores ")
        '''