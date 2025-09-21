# 🐍 Conditional Statements in Python (if/else)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-success)
![Repo Size](https://img.shields.io/github/repo-size/abjaiyad/Python-ConditionalStatements)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to this repository! 🎉  
Here, I’ve documented my learning on **Conditional Statements** in Python — one of the most important concepts in programming for making decisions.

---

## 📑 Table of Contents
- [📖 Overview](#-overview)  
- [🛠 Syntax](#-syntax)  
- [💡 Examples](#-examples)  
- [📝 Practice Exercises](#-practice-exercises)  
- [📌 Key Takeaway](#-key-takeaway)  
- [👨‍💻 Author](#-author)  

---

## 📖 Overview
Conditional statements allow programs to **decide and execute different actions** based on conditions.  
They check whether a condition is `True` or `False` and run the corresponding block of code.

---

## 🛠 Syntax
```python
if condition:
    # Executes if condition is True
else:
    # Executes if condition is False
```

---

## 💡 Examples

### ✅ if Statement
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

### ✅ if-else Statement
```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

### ✅ if-elif-else Statement
```python
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
```

### ✅ Nested if Statement
```python
number = 15
if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is Zero or Negative")
```

---

## 📝 Practice Exercises
Try solving these problems to strengthen your understanding:

1. Write a program to check if a number is positive, negative, or zero.  
2. Take a user’s age and categorize them as child, teenager, or adult.  
3. Check whether a given number is even or odd.  
4. Build a grading system:  
   - 90+ → A  
   - 75–89 → B  
   - 50–74 → C  
   - Below 50 → Fail  
5. Take a user’s name and age, then check voting eligibility.

---

## 📌 Key Takeaway
Conditional statements are the **backbone of decision-making in programming**, enabling dynamic and logical program flow.

---

## 👨‍💻 Author
**Amad Bin Jaiyad**  
📌 BCA Student | Exploring the Cutting-Edge of Technology  
🔗 [GitHub](https://github.com/abjaiyad) | [LinkedIn](https://www.linkedin.com/in/)  

---
