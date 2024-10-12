#EXAMPLES

# Define the username and password
User_name = "bimpe"  # Replace with your desired username
password = "bimpe"  # Replace with your desired password

# Prompt the user to enter their username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

# Check if the entered username and password match the predefined ones
if input_username == User_name and input_password == password:
    print("Login successful")
else:
    print("Login failed. Incorrect username or password.")


# 1.Write a program  in python that asks the user to enter a username and a password and checks if they match predefined values.If both match, print "Login successful", otherwise print "Login failed".

# Prompt user for their age
age = int(input("Enter your age: "))

# Check if the user is an adult or not
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#2. Write a program that asks the user to input a number (1-7) and prints the corresponding day of the week. Assume 1 is Monday and 7 is Sunday.
def get_day_of_week():
    # Dictionary to map numbers to days of the week
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    # Asking the user to input a number between 1 and 7
    try:
        number = int(input("Enter a number (1-7): "))
        
        if number < 1 or number > 7:
            print("Error: Number must be between 1 and 7.")
        else:
            print(f"The corresponding day of the week is: {days[number]}")
    
    except ValueError:
        print("Error: Invalid input. Please enter an integer between 1 and 7.")

# Calling the function
get_day_of_week()

# QUESTION 2 ANSWER
number = int(input("Enter a number (1-7): "))

if number == 1:
    print("Monday")
if number == 2:
    print("Tuesday")
if number == 3:
    print("Wednesday")
if number == 4:
    print("Thursday")
if number == 5:
    print("Friday")
if number == 6:
    print("Saturday")
if number == 7:
    print("Sunday")
else:
    print("Error: Number must be between 1 and 7.")


# 3 Write a program that checks the strength of a password based on the following criteria:
#At least 8 characters long
#Contains both uppercase and lowercase characters
#Contains at least one numerical digit
#Contains at least one special character (e.g., @, #, $, etc.)

    lowercase= "a-z"
    uppercase= "A-Z"
    special_character= "e.g., @, #, $, etc."
    num= "range 10"
    password = input("Enter your password: ")

if len(password) >= 8 and lowercase and uppercase and special_character and num:
    print('Password is strong.') 
else:
    print('invalid')

#Write a program that asks the user to input three numbers and prints the largest of the three.

a = 6
b = 4
c = 2

# Find the largest number
largest_number = max(a, b, c)

# Print the largest number
print('The largest number is:', largest_number)

# 4.

 # Computer randomly chooses a number between 1 and 10
import random

number = random.choice(range(1, 10))
    
    # Prompt the user to guess the number
user_guess = int(input("Guess a number between 1 and 9: "))
    
    # Check if the user's guess matches the computer's number
if user_guess == number:
        print("Congratulations! You guessed the correct number!")
else:
        print(f"Sorry, you guessed wrong. The correct number was {number}.")



#import random

# Generate a random number between 1 and 10 (inclusive)
secret_number = random.choice(range(1, 11))

# Get user guess
guess = int(input("Guess a number between 1 and 10: "))

# Check guess and print result
if guess == secret_number:
  print("You win!")
else:
  print("You lose. The number was", secret_number)


secret_number = random.choice()

# Get user guess
guess = int(input("Guess a number between 1 and 10: "))

# Check guess and print result
if guess == secret_number:
  print("You win!")
else:
  print("You lose. The number was", secret_number)



  #rock, scissor and paper game

  import random
user = input(""""             
    R for rock
    P for paper
    S for scissors
             
 """)

rps = ['rock', 'paper', 'scissors']

computer_choice = random.choice(rps)

if user == 'paper' and computer_choice == 'rock':
    print('user wins, paper covers rock')   
elif user == 'scissors' and computer_choice == 'paper':
    print('user wins, scissors cuts paper')
elif user == 'rock' and computer_choice == 'scissors':
    print('rock smashes scissors')

else:
    print('computer wins')


#rock, scissor and paper with more function

import random

print('welcome to RPS')

user_name = input('Enter your name: ')

user_name = input(""""
             
             R for rock
             P for paper
             S for scissors : 
             
             """)

rps = ['rock', 'paper', 'scissors']

computer_choice = random.choice(rps)

if user_name == 'paper' and computer_choice == 'rock':
    print('user_name wins, paper covers rock')   
    if user_name == 'scissors' and computer_choice == 'paper':
        print('user_name wins, scissors cuts paper')
    if user_name == 'rock' and computer_choice == 'scissors':
        print('rock smashes scissors')
elif computer_choice == 'paper' and user_name == 'rock':
    print(f"computer wins, paper covers rock. computer's choice was ", {computer_choice})
    if computer_choice == 'scissors' and user_name == 'paper':
        print("computer wins, Scissors, cuts paper. computer's choice was ",{computer_choice})
    if computer_choice == 'rock' and user_name == 'scissors':
        print(f"Computer wins, rock smashes scissors, computer's choice was",{computer_choice})


else:
    print('its a draw')



#added fuction to rock, paper and scissor

import random

def play_round(user_choice):
    rps = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(rps)

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print(f"{user_choice.capitalize()} wins! {user_choice.capitalize()} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice.capitalize()} beats {user_choice}.")

print('Welcome to Rock-Paper-Scissors!')

user_input = input("""
    R for rock
    P for paper
    S for scissors: 
    """).lower()

# Mapping user input to full names
choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
user_choice = choices.get(user_input, '')

if user_choice:
    play_round(user_choice)
else:
    print("Invalid choice. Please enter R, P, or S.")


#handling error

import random

print('Welcome to RPS')

user_name = input('Enter your name: ')

user_choice = input("""
    R for rock
    P for paper
    S for scissors: 
    """)

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
    elif (user_choice_full == 'paper' and computer_choice == 'rock') or \
         (user_choice_full == 'scissors' and computer_choice == 'paper') or \
         (user_choice_full == 'rock' and computer_choice == 'scissors'):
        print(f"{user_name} wins! {user_choice_full} beats {computer_choice}")
    else:
        print(f"Computer wins! {computer_choice} beats {user_choice_full}")


#adding while loop function

import random

# Initialize login attempts
login_attempts = 0

# Loop until the user has made 5 login attempts or logs in successfully
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    start = input('Enter "play" to begin the game or "exit" to quit: ')

    if start.lower() == 'exit':
        print("Exiting the program.")
        break

    if start.lower() == 'play':
        print('Welcome to RPS')

        while True:
            user_name = input('Enter your name: ')
            user_choice = input("""
                rock
                paper
                scissors: 
                """)

            rps = ['rock', 'paper', 'scissors']
            computer_choice = random.choice(rps)

            if user_choice == 'paper' and computer_choice == 'rock':
                print('User wins, paper covers rock')
            elif user_choice == 'scissors' and computer_choice == 'paper':
                print('User wins, scissors cuts paper')
            elif user_choice == 'rock' and computer_choice == 'scissors':
                print('Rock smashes scissors')
            elif computer_choice == 'paper' and user_choice == 'rock':
                print("Computer wins, paper covers rock")
            elif computer_choice == 'scissors' and user_choice == 'paper':
                print("Computer wins, scissors cuts paper")
            elif computer_choice == 'rock' and user_choice == 'scissors':
                print("Computer wins, rock smashes scissors")
            elif computer_choice == user_choice:
                print('Draw')
                continue
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                continue

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

    

#form
name = input ("enter name: ")
if len(name) <3:
    print("Name must be at least 3 characters")
elif len(name) >50:
    print("Name can be a max of 50 characters")
else:
    print("Name looks good")



