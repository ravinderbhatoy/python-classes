# Modules -> pre-written code

import random
target = random.randint(1, 100)  # generate a random integer

tries = 0
game_on = True

difficulty = input("Choose difficulty(hard/easy): ").lower()

if difficulty == 'hard':
    tries = 5
else:
    tries = 10

print(target)

while game_on:
    print(f"{tries} tries left.")
    tries -= 1

    guess = int(input("Guess the number: "))
    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        game_on = False

    if tries == 0:
        break

if tries > 0:
    print("You win!")
else:
    print("You lose!")
