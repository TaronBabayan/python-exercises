name = str(input("What is your name: "))

age = int(input("How old are you {}: " .format(name)))

if 18 <= age <= 30:
    print("welcome to the holiday {}" .format(name))
else:
    print("Sorry, not this time {}" .format(name))