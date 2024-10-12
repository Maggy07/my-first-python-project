#while loop

import random

# Initialize login attempts
login_attempts = 0

# Loop until the user has made 5 login attempts or successfully starts the game
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    
    # Prompt for game start
    start = input('Enter "play" to start the game or "exit" to quit: ')

    if start.lower() == 'exit':
        print("Exiting the program.")
        break

    if start.lower() == 'play':
        print('Welcome to RPS')

        user_name = input('Enter your name: ')

        user_choice = input("""
            R for rock
            P for paper
            S for scissors: 
            """)

        rps = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        
        if user_choice.lower() not in rps:
            print("Invalid choice. Please choose 'R' for rock, 'P' for paper, or 'S' for scissors.")
        else:
            user_choice_full = rps[user_choice.lower()]
            computer_choice = random.choice(list(rps.values()))

            print(f"{user_name} chose: {user_choice_full}")
            print(f"Computer chose: {computer_choice}")

            if user_choice_full == computer_choice:
                print("It's a draw")
            elif (user_choice_full == 'paper' and computer_choice == 'rock') or \
                 (user_choice_full == 'scissors' and computer_choice == 'paper') or \
                 (user_choice_full == 'rock' and computer_choice == 'scissors'):
                print(f"{user_name} wins! {user_choice_full} beats {computer_choice}")
            else:
                print(f"Computer wins! {computer_choice} beats {user_choice_full}")

            # Prompt for replay
            replay = input('Play again? (yes/no): ')
            if replay.lower() == 'no':
                break
            elif replay.lower() != 'yes':
                print("Invalid input. Exiting the game.")
                break

        # Increment login attempts after a game session
        login_attempts += 1
    else:
        print("Invalid input. Please enter 'play' or 'exit'.")
        login_attempts += 1

if login_attempts >= 5:
    print("Maximum login attempts reached. Exiting the program.")


##

import random

print('Welcome to RPS')

user_name = input('Enter your name: ')

user_score = 0
computer_score = 0

while True:
    user_choice = input("""
    R for rock
    P for paper
    S for scissors
    Q to quit: 
    """).lower()

    if user_choice == 'q':
        break

    rps = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    # Error handling for invalid choices
    if user_choice not in rps:
            print("Invalid choice. Please choose 'R' for rock, 'P' for paper, or 'S' for scissors.")
    else:
            user_choice_full = rps[user_choice]
            computer_choice = random.choice(list(rps.values()))
            print(f"{user_name} chose: {user_choice_full}")
            print(f"Computer chose: {computer_choice}")

            if user_choice_full == computer_choice:
                print("It's a draw")
            elif (user_choice_full == 'rock' and computer_choice == 'scissors') or \
                 (user_choice_full == 'scissors' and computer_choice == 'paper') or \
                 (user_choice_full == 'paper' and computer_choice == 'rock'):
                print(f"{user_name} wins! {user_choice_full} beats {computer_choice}")
                user_score += 1
            else:
                print(f"Computer wins! {computer_choice} beats {user_choice_full}")
                computer_score += 1
                user_score -=1

            print(f"Score:  {user_score}, Computer: {computer_score}")

            replay = input(f"{user_name}, do you want to continue? yes or no: ")
            if replay== 'yes':
                continue
            elif replay == 'no':
                break
            else:
                print('Invalid input')

print("Thanks for playing!")


#Guess game
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int (input("Guess: "))
    guess_count +=1

    if guess == secret_number:
        print("you won!")
        break
else:
    print("you loss! Game Over")


# CAR GAME
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started ...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the car
""")
    elif command == "quit":
        print("Exiting the game.")
        break
    else:
        print("Sorry, I do not understand.")

#note while is used to execute a block of code multiple times










