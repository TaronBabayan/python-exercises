import random

highest = 10

answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing

print("Please guess the number between 1 and {}" .format(highest))

guess= "a"
while guess!=answer:
    guess = int(input("Type your gusess here: ")) 
    if guess == answer:
        print("you'v got it first time")
        break
    else:
        if guess<answer:
            print("Guess higher")
        else:
            print("Guess Lower")
        
        
print("You've got it")