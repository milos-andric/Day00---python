import string
import random

print('This is an interactive guessing game!')
findph = 'and 99 to find out the secret number.'
print('You have to enter a number between 1 ' + findph)
print("Type 'exit' to end the game.")
print('Good luck!\n')
ian = "the universe and everything is 42."
ch = "The answer to the ultimate question of life, " + ian
target = random.randint(1, 99)
attempts = 1
while(1):
    print("What's your guess between 1 and 99 ?")
    number = input()
    try:
        if str(number) == "exit":
            print('Goodbye!')
            exit()
        number = int(number)
    except valueError:
        print("That's not a number.")
    if(number < target):
        print('Too low!')
    elif(number > target):
        print('Too high!')
    elif((number == target) and (attempts > 1)):
        if (target == 42):
            print(ch)
        print("Congratulations, you've got it!")
        print("You won in " + str(attempts) + " attempts")
        exit()
    elif((number == target) and (attempts == 1)):
        if(target == 42):
            print(ch)
        print("Congratulations, you've got it on your first try!")
        exit()
    attempts += 1
