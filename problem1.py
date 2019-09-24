from random import random
print("Guess the Number Game")
print(" ")
print("I\'m thinking of a number between 1 and 10")

number = round(random()*10)+1
print(number)
guessed = False
while not guessed:
    try:
        guess = int(input("What\'s your guess? "))
        if (guess == number):
            print("You guessed right!")
            guessed = True
        elif (guess < number):
            print("Your guess is too low, try again!")
        else:
            print("Your guess is too high, try again!")
    except:
        print("You suck, enter a number")
