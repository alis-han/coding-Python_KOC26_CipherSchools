import random

def replay():  
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

user_score=0
computer_score=0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("You chose:",user_action,"Computer chose:",computer_action)
    if user_action == computer_action:
        print("Both players selected same. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score+=1
        else:
            print("Paper covers rock! You lose.")
            computer_score+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score+=1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score+=1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score+=1

    print("User_Score:",user_score)
    print("Computer_Score:",computer_score)        
    
    if not replay():
        break