#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
input = "Guido"
greet(input)

def greet_with_default(name="programmer"):
    print (f"Hello, {name}!")
input = "Guido"
greet(input)

def add(num1, num2):
    return num1 + num2
result = (add(45, 55) == 100)
print(result)


def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

result = (halve(100) == 50)
print(result)  

result_invalid = halve("invalid")
print(result_invalid) 