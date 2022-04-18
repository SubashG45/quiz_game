import random


top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("enter number greater than 0 in next time")
        quit()
else:
    print("enter number next time")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("enter number next time")
        continue
    if user_guess == random_number:
        print("You go it!  ")
        break
    elif user_guess > random_number:
        print("you were above the number! ")
    else:
        print("you were below the number! ")
print("you got it in", guesses,"guesses")