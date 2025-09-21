# Author: Amad Bin Jaiyad
"""
Problem2:
         Take a user’s age and check if they are child, teenager, or adult.
"""
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("You are a chid")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20:
    print("You are a adult")
else:
    print("Invalid age entered")