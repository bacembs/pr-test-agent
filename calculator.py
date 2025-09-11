def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # BUG: No division by zero check!

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # BUG: No empty list check!

def unsafe_user_input(user_data):
    # SECURITY ISSUE: Using eval is dangerous
    result = eval(user_data)
    return result

def inefficient_search(data_list, target):
    # PERFORMANCE: O(n) search when could use better algorithm
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1