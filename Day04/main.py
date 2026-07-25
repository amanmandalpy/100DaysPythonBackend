"""
Day 04
Topic : Functions
"""

# ----------------------------
# Simple Function
# ----------------------------


def welcome():
    print("Welcome to Python Backend Challenge")


welcome()

print("-" * 50)

# ----------------------------
# Function with Parameters
# ----------------------------


def greet(name):
    print(f"Hello {name}")


greet("Aman")
greet("Rahul")

print("-" * 50)

# ----------------------------
# Function Returning Value
# ----------------------------


def add(a, b):
    return a + b


result = add(10, 20)

print("Addition =", result)

print("-" * 50)

# ----------------------------
# Default Argument
# ----------------------------


def employee(name, city="Delhi"):
    print(name, city)


employee("Aman")
employee("Rahul", "Mumbai")

print("-" * 50)

# ----------------------------
# Keyword Arguments
# ----------------------------


def student(name, age):
    print(name, age)


student(age=28, name="Aman")

print("-" * 50)

# ----------------------------
# Variable Length Arguments
# ----------------------------


def total_marks(*marks):
    print(sum(marks))


total_marks(70, 80, 90)
total_marks(50, 60)

print("-" * 50)

# ----------------------------
# Keyword Variable Arguments
# ----------------------------


def profile(**details):
    for key, value in details.items():
        print(key, ":", value)


profile(name="Aman", city="Sitarganj", language="Python")

print("-" * 50)

# ----------------------------
# Local Variable
# ----------------------------


def demo():
    message = "Local Variable"
    print(message)


demo()

print("-" * 50)

# ----------------------------
# Global Variable
# ----------------------------

company = "OpenAI"


def show_company():
    print(company)


show_company()

print("-" * 50)

# ----------------------------
# Docstring
# ----------------------------


def multiply(a, b):
    """
    Returns multiplication of two numbers.
    """
    return a * b


print(multiply(5, 4))
print(multiply.__doc__)

print("-" * 50)

# ----------------------------
# Lambda Function
# ----------------------------

square = lambda x: x * x

print(square(7))

print("-" * 50)

print("Day 04 Completed Successfully")
