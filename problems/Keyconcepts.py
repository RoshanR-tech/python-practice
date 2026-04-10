# Number Guessing Game
# Concept: while loop, if-else, user input

secret_number = 7
guess = -1

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
    else:
        print("Wrong guess, try again.")
