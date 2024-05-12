exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in exits:
    chosen_exit = input("please chose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break 
        

print("aren't you glad you got out of there")