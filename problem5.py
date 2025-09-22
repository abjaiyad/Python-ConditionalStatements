# Author: Amad Bin Jaiyad
"""
Problem5:
         Take a user’s name and age → check voting eligibility.
"""
name = input("Enter you name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote yet.")