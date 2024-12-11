"""
Object-Oriented Programming (OOP) Concepts in Python

1. **Class**: A blueprint for creating objects. Classes define the structure and behavior of objects.
2. **Object**: An instance of a class. Objects hold the actual data and methods defined by the class.
3. **Attributes**: Variables that hold data associated with an object.
4. **Methods**: Functions that define behaviors or actions an object can perform.
5. **Inheritance**: A mechanism for a class to use properties and methods from another class.
6. **Polymorphism**: The ability to redefine methods in derived classes while keeping the same interface.
7. **Encapsulation**: Restricting direct access to some of an object's attributes and methods to ensure control over data.
8. **Abstraction**: Hiding the internal details of how a task is performed while showing only the functionality.
"""

# Step 1: Create a Base Class i.e Parent Class
class Animal:
    """
    Animal is the base class (or parent class).
    It contains general attributes and methods common to all animals.
    """
    def __init__(self, name, species):
        """
        Initialize the Animal object with a name and species.
        """
        self.name = name  # Public attribute
        self.species = species  # Public attribute

    def eat(self):
        """
        Define a common behavior for animals: eating.
        """
        print(f"{self.name} is eating.")

    def sleep(self):
        """
        Define another common behavior for animals: sleeping.
        """
        print(f"{self.name} is sleeping.")

# Step 2: Create a Derived Class i.e Child Class
class Dog(Animal):
    """
    Dog is a derived class (or child class) inheriting from Animal.
    It adds specific behaviors and attributes unique to dogs.
    """
    def __init__(self, name, breed):
        """
        Initialize the Dog object with name and breed.
        Call the parent class's constructor using super().
        """
        super().__init__(name, species="Dog")  # Set species to "Dog" by default
        self.breed = breed  # New attribute specific to Dog

    def bark(self):
        """
        Define a behavior specific to dogs: barking.
        """
        print(f"{self.name}, the {self.breed}, is barking.")

# Step 3: Create Another Derived Class
class Cat(Animal):
    """
    Cat is another derived class inheriting from Animal.
    It adds unique behaviors specific to cats.
    """
    def __init__(self, name, color):
        """
        Initialize the Cat object with name and color.
        Call the parent class's constructor using super().
        """
        super().__init__(name, species="Cat")  # Set species to "Cat" by default
        self.color = color  # New attribute specific to Cat

    def meow(self):
        """
        Define a behavior specific to cats: meowing.
        """
        print(f"{self.name}, the {self.color} cat, is meowing.")

# Step 4: Use the Classes
if __name__ == "__main__":
    """
    Create instances (objects) of the classes and demonstrate their functionality.
    """
    # Create an Animal object
    generic_animal = Animal("GenericAnimal", "UnknownSpecies")
    generic_animal.eat()
    generic_animal.sleep()

    print("\n")

    # Create a Dog object
    my_dog = Dog("Buddy", "Golden Retriever")
    my_dog.eat()  # Inherited from Animal
    my_dog.sleep()  # Inherited from Animal
    my_dog.bark()  # Specific to Dog

    print("\n")

    # Create a Cat object
    my_cat = Cat("Whiskers", "Black")
    my_cat.eat()  # Inherited from Animal
    my_cat.sleep()  # Inherited from Animal
    my_cat.meow()  # Specific to Cat
