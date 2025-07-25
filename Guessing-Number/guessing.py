import random
import time 

def initialize_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    print("\n")
    print("Please select the difficulty level (write the number):")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")
    print("\n")
    difficulty = int(input("Enter your choice: "))
    print("\n")
    if difficulty == 1:
        attempts = 10
        print("Great! You have selected the Easy level.")
        print("Let's start the game!")
        print("\n")
    elif difficulty == 2:
        attempts = 5
        print("Great! You have selected the Medium level.")
        print("Let's start the game!")
        print("\n")
    elif difficulty == 3:
        attempts = 3
        print("Great! You have selected the Hard level.")
        print("Let's start the game!")
        print("\n")
    else:
        raise Exception("Invalid input. Please select a valid difficulty level.")
    random_number = random.randint(1, 100)
    return attempts, random_number

######################################################################

def play_game():
    attempts, random_number = initialize_game()
    counter = 0
    start_time = time.time()
    while attempts > 0:
        
        guess = int(input("Enter your guess: "))
        if guess != random_number:
            if guess < random_number:
                print(f"Incorrect! The number is greater than {guess}.")
                if random_number - guess <= 7:
                    print("You are very close to the correct number.")
                print("\n")
            else:
                print(f"Incorrect! The number is less than {guess}.")
                if guess - random_number <= 7:
                    print("You are very close to the correct number.")
                print("\n")
            attempts -= 1
            counter += 1
            
        else:
            counter += 1
            end_time = time.time()
            taken_time = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the correct number in {counter} attempts and {taken_time} seconds.")
            break
    if attempts == 0:
        print(f"Game Over! The correct number was {random_number}.")
        print("\n")
    
######################################################################  
        
def replay_game():
    replay = input("Do you want to play again? (yes/no): ")
    if replay.strip().lower() == "yes":
        play_game()
        replay_game()
    elif replay.strip().lower() == "no":
        print("Thank you for playing the Number Guessing Game!")
        print("\n")
    else:
        raise Exception("Invalid input. Please enter 'yes' or 'no'.")

######################################################################

if __name__ == "__main__":
    play_game()
    replay_game()