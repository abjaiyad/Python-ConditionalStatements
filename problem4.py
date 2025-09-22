# Author: Amad Bin Jaiyad
"""
Problem4:
         Create a grading system (A, B, C, Fail).
"""
marks = float(input("Enter you marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")