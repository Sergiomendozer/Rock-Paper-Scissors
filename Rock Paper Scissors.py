import random

#function loop games
def rock_paper_scissors2(user_choice):
    list_computer_chooses_from = ['Rock','Paper', 'Scissors']
    computers_choice= random.choice(list_computer_chooses_from)
    class color:
        purple ='\033[35m'
    green ='\033[32m'
    Yellow ='\033[33m'
    red ='\033[31m'
    END = '\033[0m'
    if computers_choice == 'Rock' and user_choice == "R" or computers_choice == 'Rock'and user_choice == "r" or computers_choice == 'Rock'and user_choice == "rock" or computers_choice == 'Rock'and user_choice == "Rock":
        print (Yellow +'You tied' + END) 
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Rock' and user_choice == "P" or computers_choice == 'Rock' and user_choice == "p" or computers_choice == 'Rock' and user_choice == "paper" or computers_choice == 'Rock'and user_choice == "Paper":
        print( green +'Paper beats Rock, you win!' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Rock' and user_choice == "S" or computers_choice == 'Rock' and user_choice == "s" or computers_choice == 'Rock'and user_choice == "scissors" or computers_choice == 'Rock' and user_choice == "Scissors":
        print(red + "Rock beats Scissors, you lose."+ END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "P" or computers_choice == 'Paper' and user_choice == "p" or computers_choice == 'Paper' and user_choice == "paper" or computers_choice == 'Paper' and user_choice == "Paper":
        print (Yellow +'You tied' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "R" or computers_choice == 'Paper' and user_choice == "r" or computers_choice == 'Paper' and user_choice == "rock" or computers_choice == 'Paper' and user_choice == "Rock":
        print(red +'Paper beats Rock you lose' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "S" or computers_choice == 'Paper' and user_choice == "s" or computers_choice == 'Paper' and user_choice == "scissors" or computers_choice == 'Paper' and user_choice == "Scissors":
        print(green + "Scissors beats Paper, you win!")
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "S" or computers_choice == 'Scissors' and user_choice == "s" or computers_choice == 'Scissors' and user_choice == "scissors" or computers_choice == 'Scissors' and user_choice == "Scissors":
        print (Yellow +'You tied' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "P" or computers_choice == 'Scissors' and user_choice == "p" or computers_choice == 'Scissors' and user_choice == "paper" or computers_choice == 'Scissors' and user_choice == "Paper":
        print (red + " Scissors beats Paper, you lose." + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "R" or computers_choice == 'Scissors' and user_choice == "r" or computers_choice == 'Scissors' and user_choice == "rock" or computers_choice == 'Scissors' and user_choice == "Rock":
        print (green + "Rock beats Scissors, you win!" + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())

#
def rock_paper_scissors(computers_choice, user_choice):
    class color:
        purple ='\033[35m'
    green ='\033[32m'
    Yellow ='\033[33m'
    red ='\033[31m'
    END = '\033[0m'
    if computers_choice == 'Rock' and user_choice == "R" or computers_choice == 'Rock'and user_choice == "r" or computers_choice == 'Rock'and user_choice == "rock" or computers_choice == 'Rock'and user_choice == "Rock":
        print (Yellow +'You tied' + END) 
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Rock' and user_choice == "P" or computers_choice == 'Rock' and user_choice == "p" or computers_choice == 'Rock' and user_choice == "paper" or computers_choice == 'Rock'and user_choice == "Paper":
        print( green +'Paper beats Rock, you win!' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Rock' and user_choice == "S" or computers_choice == 'Rock' and user_choice == "s" or computers_choice == 'Rock'and user_choice == "scissors" or computers_choice == 'Rock' and user_choice == "Scissors":
        print(red + "Rock beats Scissors, you lose."+ END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "P" or computers_choice == 'Paper' and user_choice == "p" or computers_choice == 'Paper' and user_choice == "paper" or computers_choice == 'Paper' and user_choice == "Paper":
        print (Yellow +'You tied' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "R" or computers_choice == 'Paper' and user_choice == "r" or computers_choice == 'Paper' and user_choice == "rock" or computers_choice == 'Paper' and user_choice == "Rock":
        print(red +'Paper beats Rock you lose' + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Paper' and user_choice == "S" or computers_choice == 'Paper' and user_choice == "s" or computers_choice == 'Paper' and user_choice == "scissors" or computers_choice == 'Paper' and user_choice == "Scissors":
        print(green + "Scissors beats Paper, you win!")
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "S" or computers_choice == 'Scissors' and user_choice == "s" or computers_choice == 'Scissors' and user_choice == "scissors" or computers_choice == 'Scissors' and user_choice == "Scissors":
        print (Yellow +'You tied' + END) 
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "P" or computers_choice == 'Scissors' and user_choice == "p" or computers_choice == 'Scissors' and user_choice == "paper" or computers_choice == 'Scissors' and user_choice == "Paper":
        print (red + " Scissors beats Paper, you lose." + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
    elif computers_choice == 'Scissors' and user_choice == "R" or computers_choice == 'Scissors' and user_choice == "r" or computers_choice == 'Scissors' and user_choice == "rock" or computers_choice == 'Scissors' and user_choice == "Rock":
        print (green + "Rock beats Scissors, you win!" + END)
        print ("Play again,Select between Rock(R), Paper(P) or Scissors(S):")
        return rock_paper_scissors2(input())
def start (play):
    if play == 'p':
        # a list between Rock, Paper, Scissors to have computer randomly choose
        list_computer_chooses_from = ['Rock','Paper', 'Scissors']
        computers_choice= random.choice(list_computer_chooses_from)
        user_choice = input("Select between Rock(R), Paper(P) or Scissors(S): ")
        return rock_paper_scissors(computers_choice, user_choice)

#prompt user to start playing rock, paper, scissors
play = str(input("To play rock, paper, scissors enter p, and press enter: "))
start(play)
