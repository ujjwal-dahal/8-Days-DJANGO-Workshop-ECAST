

# Understanding Classes, Objects, and Constructors in Python

# A class is a blueprint for creating objects (instances of the class).
class Person:
    """
    This class represents a person with a name and age.
    """

    # Constructor (__init__ method) initializes the attributes of the class.
    def __init__(self, name, age):
        """
        Constructor to initialize name and age.
        :param name: Name of the person.
        :param age: Age of the person.
        """
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    # Method to display person's details.
    def display_details(self):
        """
        Prints the details of the person.
        """
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects (instances) of the Person class.
person1 = Person("Alice", 25)  # Object creation with name and age
person2 = Person("Bob", 30)

# Accessing methods and attributes of the objects.
person1.display_details()  # Output: Name: Alice, Age: 25
person2.display_details()  # Output: Name: Bob, Age: 30

# Updating attributes of an object.
person1.age = 26  # Changing Alice's age
person1.display_details()  # Output: Name: Alice, Age: 26
