import random
print("Welcome to the Number Guessing Game!")
while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        if attempts == 7:
            print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
            break
    again= input("Do you want try again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing! Goodbye.")
        break
    else:
        print("Starting a new game...")