# 1. Built-in Functions
# Python has many built-in functions that you can use directly.
# Example: len() function to get the length of a list

my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4, because the list has 4 elements

# Example: type() function to get the type of a variable
print(type(my_list))  # Output: <class 'list'>, as my_list is a list


# 2. User-Defined Functions
# You can define your own functions using the 'def' keyword.
def greet(name):
    """This function greets the user with the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!




# 3. Lambda (Anonymous) Functions
# Lambda functions are anonymous and are defined using the 'lambda' keyword.
# They're typically used for short functions that are used only once.
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8, as it adds 5 and 3




# 4. Recursive Functions
# A recursive function is a function that calls itself to solve smaller parts of a problem.
# Example: Calculate factorial using recursion
def factorial(n):
    """This function calculates the factorial of a number recursively."""
    if n == 1:  # Base case: if n is 1, return 1
        return 1
    return n * factorial(n - 1)  # Recursive call with a smaller value of n

print(factorial(5))  # Output: 120, as factorial of 5 is 5*4*3*2*1
