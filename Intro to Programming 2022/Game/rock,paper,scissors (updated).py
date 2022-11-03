#Sources: 
# Mr Cozort's canvas page
# https://www.w3schools.com/python/default.asp
# https://realpython.com/

from random import * 
# template used from Mr. Cozort


myList = ["Rock", "Paper", "Scissors"]
loop = True


def computer_choice():
    global computer_decision
    randNum = randint(0,2)
    # picks one random one out of 0-2 (means all three items in list)
    computer_decision = print(myList[randint(0, len(myList)-1)])
    # computer's choice is random from mylist
    # allows me to take one object out of my list or add one to it without any issues

def user_Des():
    global user_decision
    user_decision = input("Enter Rock Paper or Scissors").lower()
#ask user to interact + computer to respond to user's interaction

    
def establish_winner():
    if user_decision == computer_decision:
            print("We both chose the same object, therefore it's a tie")
    elif user_decision == "rock":
        if computer_decision == "paper":
            print("I win, You lose!")
        if computer_decision == "scissors":
            print("Oh man, I lost! You win")
    elif user_decision == "paper":
        if computer_decision == "rock":
            print("Oh wow, you won")
        if computer_decision == "paper":
            print("We tied!")
        if computer_decision == "scissors":
            print("I can't believe it, you won")
    elif user_decision == "scissors":
        if computer_decision == "rock":
            print("Yes! You lost")
        if computer_decision == "paper":
            print("You won, you got lucky!")
        if computer_decision == "scissors":
            print("It's a tie")

 # establish the win or lose situations through if-else statements

def user_selection():
    global loop
    rematch = input("Want to play again? Enter: Yes or No) ")
    if rematch.lower() != "yes":
                print("Goodbye, Thank you for playing with me")
                loop = False
# game reacts to user imput 
                
    else:
        return
                

print("Hello user,", "Would you like to play a game of Rock, Paper, Scissors")
welcome_user = input("Enter Yes or No: ")
if welcome_user.lower() == "yes":
            print ("Perfect, let's play!")
            while loop == True:
                user_Des()
                computer_choice()
                establish_winner()
                user_selection()
# call all the functions --> do what theyt are supposed to do 
# through flow control more control over code

elif welcome_user != "yes":
            print("Goodbye, Thank you for playing with me")
# game reacts to user imput 


    
       
        
        
           
     

        
        
        
       

        
            



            