# Modules -> pre-written code

# import random
# random.randint(1, 101)

from random import randint


def guessing():
    target = randint(1, 101)
    print(target)

    difficulty = input("Choose difficulty level(hard/easy): ").lower()
    tries = 10

    if difficulty == 'hard':
        tries = 5

    game_on = True

    while game_on:
        print(f"{tries} tries left")
        guess = int(input("Guess the number: "))
        if guess == target:
            game_on = False
        else:
            if guess > target:
                print("Guess lower")
            elif guess < target:
                print("Guess higher")
            tries -= 1

        if tries == 0:
            game_on = False

    if tries == 0:
        print("You ran out of tries You lose!")
    else:
        print("You win!")


guessing()
while True:
    play_again = input("Do you want to play again (y/n): ")
    if play_again == 'y':
        guessing()
    else:
        break

print("Thank you for playing!!")
