import random

print("Hello, welcome to number guessing game!\nYou have 7 chances to guess the number. Let's start!")

print("Enter the lower bound:")
lower_border = int(input())

print("Enter the higher bound:")
higher_border = int(input())

number = random.randint(lower_border, higher_border)

chances = 7
guessing_counter = 0

print(f"You have 7 chances to gues number between {lower_border} and {higher_border}. Let's start!")

while guessing_counter < chances:
    guessing_counter += 1

    print("Enter your guess:")
    guess = int(input())

    if guess == number:
        print(f"Correct! The number is {guess}. You guessed it in {guessing_counter} attempts.")
        break

    elif guessing_counter >= chances and guess != number:
        print(f"Sorry! The number was {number}. Better luck next time.")
        break


    elif guess > number:
        print("Too high! Try lower number.")

    elif guess < number:
        print("Too low! Try a higher number.")