import random

x = input("Please type rock, paper, or scissors: ")
n = random.randint(1,3)

if n == 1:
    player2_choice = "rock"
    
elif n == 2:
    player2_choice = "paper"
    
else:
    player2_choice = "scissors"

print("The computer chooses " + player2_choice + ".")



if player2_choice == "rock" and x == "rock":
    print("The game is a tie.")

elif player2_choice == "paper" and x == "paper":
    print("The game is a tie.")
    
elif player2_choice == "scissors" and x == "scissors":
    print("The game is a tie.")
    
elif player2_choice == "rock" and x == "paper":
    print("Paper beats rock. You win!")

elif player2_choice == "rock" and x == "scissors":
    print("Rock beats scissors. Computer wins!")

elif player2_choice == "paper" and x == "rock":
    print("Paper beats rock. Computer wins!")

elif player2_choice == "paper" and x == "scissors":
    print("Scissors beats paper. You win!")

elif player2_choice == "scissors" and x == "rock":
    print("Rock beats scissors. You win!")

else:
    print("Scissors beats paper. Computer wins!")
