# Understanding *args and **kwargs in Python

# *args allows a function to accept any number of positional arguments.
def sum_numbers(*args):
    """
    This function sums up all the numbers passed as positional arguments.
    :param args: A tuple of all the arguments passed.
    """
    print("Positional arguments (args):", args)
    return sum(args)

# Example usage of *args:
result = sum_numbers(1, 2, 3, 4, 5)  # Passing multiple positional arguments
print("Sum of numbers:", result)


# **kwargs allows a function to accept any number of keyword arguments.
def print_person_details(**kwargs):
    """
    This function prints out key-value pairs of keyword arguments.
    :param kwargs: A dictionary of all the keyword arguments passed.
    """
    print("Keyword arguments (kwargs):", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage of **kwargs:
print_person_details(name="Alice", age=25, country="USA")  # Passing multiple keyword arguments


# Combining *args and **kwargs in a single function.
def greet_people(*args, **kwargs):
    """
    This function demonstrates the use of both *args and **kwargs.
    :param args: Positional arguments.
    :param kwargs: Keyword arguments.
    """
    print("\n-- Greeting People --")
    for name in args:
        print(f"Hello, {name}!")

    print("\nDetails about each person:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage of both:
greet_people("Bob", "Charlie", city="New York", hobby="Cycling")
