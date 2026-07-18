'''
Day 01 
Topic: Variables, DataTypes, input and conversion
'''


# Variables

name = "Aman"
age = 30
salary = 450000.50
is_python_developer = True


print("Variables")
print(name)
print(age)
print(salary)
print(is_python_developer)

print("-"*50)


# Type Checking

print("Type Checking")

print(type(name))
print(type(age))
print(type(salary))
print(type(is_python_developer))

print("-" * 50)


# Memory Address

print("Memory Address")

print(id(name))
print(id(age))

print("-"*50)


# Multiple Assignment

city, state, country = "Haldwani", "Uttarakhand", "india"

print(city)
print(state)
print(country)


print("-" * 50)


# Constants

PI = 3.141

print("PI =", PI)

print("-" * 50)


# User Input

user_name = input("Enter your name: ")
user_age =input("Enter your age: ")
user_salary = float(input("Enter your salary: "))

print("-" * 50)


# f-string

print(f"My name is {user_name}.")
print(f"My age is {user_age}.")
print(f"My salary is {user_salary}")

print("-" * 50)


# Arithmetic

next_year_age = user_age + 1
print(f"Next year your age will be {next_year_age}")

print("-" * 50)
