answer = 5

print("Please guess the number between 1 and 10")

guess = int(input())
if guess == answer:
    print("You've got it first time")
else: 
    if guess<answer:
        print("Try higher")
    else: 
        print("Try lower")
    guess=int(input())
    if guess!=answer:
        print("Wrong answer")
    else:
        print("Well done")    


