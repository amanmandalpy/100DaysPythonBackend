"""
Day 02
Topic:
Operators & Conditional Statements

Author: Aman Mandal
"""

print("=" * 50)
print("Arithmetic Operators")
print("=" * 50)

a = 20
b = 6

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Power :", a**b)

print("\n" + "=" * 50)
print("Comparison Operators")
print("=" * 50)

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("\n" + "=" * 50)
print("Logical Operators")
print("=" * 50)

age = 25
salary = 50000

print(age > 18 and salary > 30000)
print(age > 30 or salary > 30000)
print(not age > 18)

print("\n" + "=" * 50)
print("Assignment Operators")
print("=" * 50)

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x //= 2
print(x)

print("\n" + "=" * 50)
print("Membership Operators")
print("=" * 50)

language = "Python"

print("P" in language)
print("Java" not in language)

print("\n" + "=" * 50)
print("Identity Operators")
print("=" * 50)

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

print("\n" + "=" * 50)
print("If Statement")
print("=" * 50)

marks = int(input("Enter Marks: "))

if marks >= 40:
    print("Pass")

print("\n" + "=" * 50)
print("If Else")
print("=" * 50)

age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

print("\n" + "=" * 50)
print("If Elif Else")
print("=" * 50)

percentage = float(input("Enter Percentage: "))

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")

print("\n" + "=" * 50)
print("Nested If")
print("=" * 50)

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

print("\n" + "=" * 50)
print("Ternary Operator")
print("=" * 50)

age = int(input("Enter Age Again: "))

message = "Adult" if age >= 18 else "Minor"

print(message)

print("\nDay 02 Completed Successfully.")
