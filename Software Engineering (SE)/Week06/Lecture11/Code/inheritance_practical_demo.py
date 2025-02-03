"""
Employee Management System with Inheritance

This program demonstrates the use of inheritance in Python to model a simple employee management system. 
It includes a base class `Employee` with common functionality for all employees and two derived classes, 
`Manager` and `Developer`, which extend the functionality of the base class. 

Key Concepts Covered:
- Class inheritance
- Using `super()` to reuse and extend base class methods
- Overriding methods in derived classes
- Adding new attributes and methods specific to derived classes
"""

# Base class Employee
class Employee:
    """
    Represents a generic employee in the company.

    Attributes:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
    """
    def __init__(self, name, salary):
        """
        Initializes an Employee with a name and salary.

        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.salary = salary

    def work(self):
        """
        Prints a generic message indicating the employee is working.
        """
        print(f"{self.name} is working.")

    def calculate_bonus(self, rate=0.1):
        """
        Calculates and prints the bonus for the employee.

        Args:
            rate (float): The bonus rate as a percentage (default is 10%).

        Returns:
            float: The calculated bonus.
        """
        bonus = self.salary * rate
        print(f"{self.name}'s bonus: {bonus}")
        return bonus

    def display_details(self):
        """
        Prints the details of the employee, including their name and salary.
        """
        print(f"Name: {self.name}, Salary: {self.salary}")


# Derived class Manager
class Manager(Employee):
    """
    Represents a Manager, a type of Employee with additional responsibilities.

    Attributes:
        team_size (int): The size of the manager's team.
    """
    def __init__(self, name, salary, team_size):
        """
        Initializes a Manager with a name, salary, and team size.

        Args:
            name (str): The name of the manager.
            salary (float): The salary of the manager.
            team_size (int): The size of the manager's team.
        """
        super().__init__(name, salary)  # Call the constructor of the base class
        self.team_size = team_size

    def work(self):
        """
        Prints a message indicating the manager is working and managing a team.
        """
        super().work()  # Call the base class work method
        print(f"Manager is managing a team of {self.team_size} members.")

    def calculate_bonus(self, rate=0.4):
        """
        Calculates a higher bonus for managers.

        Args:
            rate (float): The bonus rate as a percentage (default is 40%).

        Returns:
            float: The calculated bonus.
        """
        return super().calculate_bonus(rate)  # Call the base class calculate_bonus method

    def display_details(self):
        """
        Prints the details of the manager, including their team size.
        """
        super().display_details()  # Call the base class display_details method
        print(f"Team Size: {self.team_size}")


# Derived class Developer
class Developer(Employee):
    """
    Represents a Developer, a type of Employee with technical skills.

    Attributes:
        programming_language (str): The primary programming language of the developer.
    """
    def __init__(self, name, salary, programming_language):
        """
        Initializes a Developer with a name, salary, and programming language.

        Args:
            name (str): The name of the developer.
            salary (float): The salary of the developer.
            programming_language (str): The primary programming language of the developer.
        """
        super().__init__(name, salary)  # Call the constructor of the base class
        self.programming_language = programming_language

    def work(self):
        """
        Prints a message indicating the developer is working and coding.
        """
        super().work()  # Call the base class work method
        print(f"Developer is writing code in {self.programming_language}.")

    def display_details(self):
        """
        Prints the details of the developer, including their programming language.
        """
        super().display_details()  # Call the base class display_details method
        print(f"Programming Language: {self.programming_language}")


# Test the classes
manager = Manager("Alice", 80000, 10)  # Create a Manager instance
developer = Developer("Bob", 60000, "Python")  # Create a Developer instance

# Using base and overridden methods
print("Manager Details:")
manager.display_details()  # Print manager details
manager.calculate_bonus()  # Calculate and print manager's bonus
manager.work()  # Call manager's work method

print("\nDeveloper Details:")
developer.display_details()  # Print developer details
developer.calculate_bonus()  # Calculate and print developer's bonus
developer.work()  # Call developer's work method
