from register import *
from login import *

def main():
    flag = False
    player=''
    while flag == False:
        if askYesOrNo("Are you an registered user?"):
            player=login_user()
        else:
            player=register_user()
        if player != "":
            flag = True
        else:
            print("Sorry! Either the username or password is wrong, Please register or login again.")
    print(player)
    player.create_character()


def askYesOrNo(question):
    flag = False
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


if __name__ == "__main__":
    main()