parrot = "Norwegian BLue"

letter = input("Enter a character: ")

if letter not in parrot:
     print("I don't need that letter")
else:
     print("{} is in {}" .format(letter, parrot))