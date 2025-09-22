# Author: Amad Bin Jaiyad
"""
Problem3:
         Check whether a number is even or odd.
"""
Num = float(input("Enter a number: "))

result = "Even" if Num % 2 == 0 else "Odd"
print("Number", Num, "is:" ,result)