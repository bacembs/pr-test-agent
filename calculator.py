def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)