
import random

game_end  = False


options = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper, Scissors!")
print(" You will be playing the imfamaus Claud Compter, Known for his ability to always win rock, paper, scissors. (Weird name for a guy, don't you think?")
print(" The rules are: Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
print(" If you win, you become the World Champion of Rock, Paper, Scissors!")
facts = ["""The earliest form of "rock paper scissors"-style game originated in China and was subsequently imported into Japan, where it reached its modern standardized form, before being spread throughout the world in the early 20th century. A simultaneous, zero-sum game, it has three possible outcomes: a draw, a win, or a loss.\n""" ,
        
"""Rock Paper Scissors is considered the oldest hand game in the world, being invented during the reign of the Han dynasty.\n"""]
z = random.choice(facts)
print("in fact, " + z)

print("Why Do we care about these facts? I have no Idea! Let's play!\n")

while not game_end:
    user_choice = input("Choose Rock, Paper, or Scissors: (write the whole word without caps)\n ")
    
    computer_choice = random.choice(options)
    
    
    
    print("You chose: ", user_choice)
    
    print("Computer chose: ", computer_choice)
    
    def you_win():
        print(" Computer : No, no, No! This was all luck! Nobody has ever beaten me! I am the best! I demand a rematch!\n")
        user_input = input("Do you want to play again? (y/n): ")
        if user_input == "y":
            game_end = False
        if user_input == "n":
            game_end = True
    
    
    if user_choice == computer_choice:
    
        print("It's a tie!")
    
    elif user_choice == "Rock" and computer_choice == "Scissors":
    
        print("You win!\n")
        you_win()
    elif user_choice == "Paper" and computer_choice == "Rock":
    
        print("You win!\n")
        you_win()
    elif user_choice == "Scissors" and computer_choice == "Paper":
    
        print("You win!\n")
        you_win()
    else:
    
        print("Computer wins!\n")
        print(" Computer :Ha ha! I knew nobody could ever beat me, I am the best!")
        game_end = True
    