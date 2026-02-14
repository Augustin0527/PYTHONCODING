import random
def display_rules():
    print("/n GAME RULES")
    print("rock beats scissors")
    print("scissors beats paper")
    print(" paper beats rock n/ ")
def determine_winner(user,computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
def rock_paper_scissors():
    total_choices = ["rock" "paper" "scissors" ]
    while True:
         user_score= 0  
         computer__score= 0
         round_number= 1
         print ("\n welcome to the rock paper scissor game!")
         print("type 'rules' to see how play")   
    
                    