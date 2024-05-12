import random

highest = 10

answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing

print("Please guess the number between 1 and {}" .format(highest))

guess = int(input("Type your gusess here: "))
while guess!=answer:
    if guess<answer:
        print("Guess higher")
        guess = int(input("Type your gusess here: "))   

    else:
        print("Guess Lower")
        guess = int(input("Type your gusess here: "))
        
print("You've got it")

# if guess != answer:
#     if guess < answer:
#         print("Try higher")
#     else:
#         print("Try lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#          print("Wrong answer")
# else:
#     print("You've got it first time") 
    
# if guess > answer:
#     print("try lower")
#     guess = int(input())
#     if guess==answer:
#         print("Well done")
#     else:
#         print("sorry wrong answer")
# elif guess < answer:
#     print("try higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry wrong answer")
# else:
#     print("Definetely!!")
