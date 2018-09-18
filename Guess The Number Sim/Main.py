import time
import random
import os
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Guess The Number!")



#    ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗     ██╗
#   ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██║
#   ██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║
#   ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ╚═╝
#   ╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ██╗
#    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝




#############       All the "time.sleep()"  are just for the UX.        #############



#def StartingMsg():

time.sleep(0.5)
print("Hello! What's your name?")
user_name = str(input())
time.sleep(0.5)
print("Hello", user_name,",", "would you like to play the 'Gues The Number' game with me?")


user_asnwer = str(input())



# Starts the different cases a user can input.

yes = {'yes', 'y', 'Yes', 'Y', 'Yeah', 'yeah', 'yess', 'Yess', 'yes!', 'y!', 'Yes!', 'Y!', 'Yeah!', 'yeah!', 'yess!', 'Yess!'}
no = {'no', 'n', 'N', 'No', 'Noo', 'noo', 'no!', 'n!', 'N!', 'No!', 'Noo!', 'noo!'}




def SimProcss():

    print("Ok. I now have a number in my mind. Can you try to guess it?")
    user_answer_to_the_game_quest = input("")

    #if 






def beforeSimulatorProcss():
    
    os.system('cls')
    user_answer_2 = input("Would you like to see the 'How to Play' tab?\n")



    if user_answer_2 in yes:
        time.sleep(2)
        print("""This game, is a guessing game. It is fully based on luck.  I'll choose a number that my random generator will generate and I will give you hints, wether you are close enough, or not, like 'HOT' if you are close to my number, and 'COLD' if you are not.""")
        time.sleep(8)

        user_before_game = input("Now, shall we continue to our game?")

        if user_before_game in yes:
          SimProcss()


    elif user_answer_2 in no:
        time.sleep(1)
        print("Ok. Starting the game!")
        time.sleep(5)
        SimProcss()
    
    else:
        print("Not valid answer. Questioning again...") 
        time.sleep(2)
        beforeSimulatorProcss()



if user_asnwer in yes:
    time.sleep(0.5)
    print("Starting Simulator!")
    time.sleep(2)
    beforeSimulatorProcss()

elif user_asnwer in no:
    print("Okay! Nice to see you,", user_name, "!")

else:
    print("No answer or valid answer. Killing program...")




    



# // TODO: Add different levels. (Like from 1-10 EASY, 1-20 MEDIUM, 1-30 HARD and 1-50 EXTREME!)