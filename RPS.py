import random

your_wins = 0
my_wins = 0

playable = ["rock", "paper", "scissors"]

print("Hello!!!")
while True:
    user_input = input("Choose Rock, Paper, Scissors or Quit to leave: ")
    if user_input == "quit":
        break
    if user_input not in playable:
        print("Not a valid input! Try Again!")
        continue

    random_number = random.randint(0,2)
    my_choice = playable[random_number]
    print("I choose:", my_choice)

    if user_input == "rock" and my_choice == "scissors":
        print("\nYou won!!!")
        your_wins == 1
        continue

    elif user_input == "paper" and my_choice == "rock":
        print("\nYou won!!!")
        my_wins == 1
        continue

    elif user_input == "scissors" and my_choice == "paper":   
        print("\nYou won!!!")
        my_wins == 1
        continue

    else: 
        print("\nYou lost :(\n")
        your_wins += 1

print("You won ", your_wins, " time(s)")
print("I won ", my_wins, " time(s)\n")
print("Thank you for playing!!!")


