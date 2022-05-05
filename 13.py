import random

while True:
    level = input("Level:")
    try:
        level = int(level)
    except ValueError:
        continue

    if level >=1:
        break
if level >1:
    random_num = random.randrange(1, level)
else:
    random_num = 1

while True:
    try:
        guess = input("Guess:")
        guess = int(guess)
    except ValueError:
        continue

    if guess == random_num:
        print("Just Right!")
        break
    elif guess > random_num:
        print("Too large!")
        continue
    else:
        print("Too Small!")
        continue