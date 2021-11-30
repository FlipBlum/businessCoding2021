import random

#representation of player points
player = 0
cpu = 0

#Start of the game
print("Three points to win the game!")

#do the following if the game is not finished
while player < 3 and cpu < 3:
    cpu_choice = random.choice(["rock","paper","scissors"])
    player_choice = input("Rock, paper, or scissors:")

#using f-string as it it cleaner
#outputs both choices
    print(f"Cpu: {cpu_choice} VS Player: {player_choice}")

#differentiation between different choices
#decides on who won the round
    if player_choice.lower() == cpu_choice.lower():
        print("Tie! No points")
    elif player_choice.lower() == "rock":
        if cpu_choice == "scissors":
            player += 1
            print("Player wins! One Point!")
        elif cpu_choice == "paper":
            cpu += 1
            print("CPU Wins! One Point!")
    elif player_choice.lower() == "scissors":
        if cpu_choice == "paper":
            player += 1
            print("Player wins! One Point!")
        elif cpu_choice == "rock":
            cpu += 1
            print("CPU Wins! One Point!")
    elif player_choice.lower() == "paper":
        if cpu_choice == "rock":
            player += 1
            print("Player wins! One Point!")
        elif cpu_choice == "scissors":
            cpu += 1
            print("CPU Wins! One Point!")
    else:
        print("invalid input! New round")

#when plaer or cpu reaches 3 points, print the following
#shorter version of if statement
print("Player wins!" if player > cpu else "CPU wins")