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

def process_user_data(user_input, admin_password):
    # SECURITY: Password in plain text comparison
    if admin_password == "admin123":
        # SECURITY: SQL injection vulnerability
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        return query
    return None

def memory_leak_function(data):
    # PERFORMANCE: Memory leak - list keeps growing
    global_cache = []
    for item in data:
        global_cache.append(item * 2)
        # BUG: Never clearing the cache
    return global_cache[-1] if global_cache else None