name = input("Please input your name: ")
age = int(input("How old are you {} " .format(name)))
print(age) 

# if age>= 18:
#     print("You are old enough to buy an alcohol")
# else:
#     print("Please come back in {}  years" .format(18-age))

if age<18:
    print("Please come back in {}  years" .format(18-age))
elif age == 900:
    print("Sorry, Yoda")
else:
    print("You are old enough to buy an alcohol")