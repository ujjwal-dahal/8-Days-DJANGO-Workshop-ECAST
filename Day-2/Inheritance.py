class User:
    """
    User class to handle basic user information and methods.
    """
    def __init__(self, userName=None):
        """
        Initialize the User object with a name. Default name is None.
        """
        self.userName = userName

    def get_user_name(self):
        """
        Prompt the user to enter their name and assign it to the userName attribute.
        """
        user_name = input("Enter Your Name: ")
        self.userName = user_name

    def display_user_name(self):
        """
        Display the user's name.
        """
        print(f"Your name is {self.userName}")


class Student(User):
    """
    Student class that inherits from the User class.
    """
    def __init__(self, student_name=None):
        """
        Initialize the Student object.
        Call the parent class constructor to set the userName attribute.
        """
        super().__init__(student_name)  # Call the User class constructor

    def assign_student_name(self):
        """
        Use the get_user_name function from the User class to assign a name.
        """
        print("Assigning a name to the student...")
        self.get_user_name()  # Call the inherited method to set the name

    def display_student_name(self):
        """
        Display the student's name using the inherited userName attribute.
        """
        print(f"Student Name: {self.userName}")


# Main program
if __name__ == "__main__":
    """
    Demonstrate the functionality of User and Student classes.
    """
    # Create a Student object
    student_obj = Student()  # No name provided initially

    # Assign a name to the student using the inherited get_user_name method
    student_obj.assign_student_name()

    # Display the student's name using both parent and child class methods
    student_obj.display_user_name()  # From User class
    student_obj.display_student_name()  # From Student class
