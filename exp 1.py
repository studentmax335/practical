class Student:
    """Represents a student with basic academic attributes."""

    def __init__(self, name, roll_number, branch):
        """Constructor to initialize the student object."""
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
        print(f"Student object created for: {self.name}")

    def display_details(self):
        """Displays the details of the student."""
        print("-" * 30)
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
        print("-" * 30)

# 1. Create multiple objects (instances) of the Student class
student1 = Student("Alia Bhatt", "CS101", "Computer Science")
student2 = Student("Ranbir Kapoor", "ME205", "Mechanical Engineering")
student3 = Student("Deepika Padukone", "EC312", "Electronics and Communication")

# 2. Display the details of the objects
print("\n--- Student Details ---")
student1.display_details()
student2.display_details()
student3.display_details()
