# employees_definitions.py
"""
This module defines the Employee class hierarchy, including subclasses for different roles
and mixins for adding technical and management skills.
"""

class Employee:
    """
    Base class representing an employee.

    Attributes:
        name (str): The name of the employee.
        id (str): The ID of the employee.
        salary (float): The salary of the employee.
    """
    def __init__(self, name: str, id: str, salary: float):
        """
        Initializes an Employee object.
        """
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self) -> str:
        """
        Returns a string representation of the employee (for `print`).
        """
        return f"{self.name} (ID: {self.id})"

    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the employee (for debugging).
        """
        return f"(name='{self.name}', id='{self.id}', salary={self.salary})"

    def __lt__(self, other) -> bool:
        """
        Compares two employees based on their salary (less than).
        """
        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        """
        Compares two employees based on their salary (greater than).
        """
        return self.salary > other.salary

    def work(self):
        """
        Returns a generic work description for an employee.
        """
        return "Employee is working on tasks."

# Mixins for adding capabilities (not meant to be instantiated directly)
class TechnicalSkills:
    """
    Mixin class for adding technical skills to an employee.

    Attributes:
        certifications (list): A list of certifications the employee holds.
    """
    def __init__(self, certifications):
        """
        Initializes TechnicalSkills.
        """
        self.certifications = certifications

    def get_tech_info(self) -> str:
        """
        Returns a string containing the employee's certifications.
        """
        return f"Certifications: {', '.join(self.certifications)}"

class ManagementSkills:
    """
    Mixin class for adding management skills to an employee.

    Attributes:
        leadership_level (int): The employee's leadership level.
    """
    def __init__(self, leadership_level: int):
        """
        Initializes ManagementSkills.
        """
        self.leadership_level = leadership_level

    def get_management_info(self) -> str:
        """
        Returns a string containing the employee's leadership level.
        """
        return f"Leadership Level: {self.leadership_level}"

# Employee subclasses inheriting from Employee and mixins
class Developer(Employee, TechnicalSkills):
    """
    Represents a developer employee. Inherits from Employee and TechnicalSkills.

    Attributes:
        programming_languages (list): A list of programming languages the developer knows.
    """
    def __init__(self, name: str, id: str, salary: float, programming_languages, certifications):
        """
        Initializes a Developer object.
        """
        Employee.__init__(self, name, id, salary) # Initialize the Employee part
        TechnicalSkills.__init__(self, certifications) # Initialize the TechnicalSkills part
        self.programming_languages = programming_languages

    def work(self):
        """
        Returns a work description specific to a developer.
        """
        return f"{self.name} is coding in {', '.join(self.programming_languages)}."

class TeamLead(Employee, ManagementSkills):
    """
    Represents a team lead employee. Inherits from Employee and ManagementSkills.

    Attributes:
        team_size (int): The size of the team the team lead manages.
    """
    def __init__(self, name: str, id: str, salary: float, team_size: int, leadership_level: int):
        """
        Initializes a TeamLead object.
        """
        Employee.__init__(self, name, id, salary)
        ManagementSkills.__init__(self, leadership_level)
        self.team_size = team_size

    def work(self):
        """
        Returns a work description specific to a team lead.
        """
        return f"{self.name} is managing a team of {self.team_size} members."

class Manager(Employee, ManagementSkills):
    """
    Represents a manager employee. Inherits from Employee and ManagementSkills.

    Attributes:
        department (str): The department the manager oversees.
    """
    def __init__(self, name: str, id: str, salary: float, department: str, leadership_level: int):
        """
        Initializes a Manager object.
        """
        Employee.__init__(self, name, id, salary)
        ManagementSkills.__init__(self, leadership_level)
        self.department = department

    def work(self):
        """
        Returns a work description specific to a manager.
        """
        return f"{self.name} is overseeing the {self.department} department."

class BusinessAnalyst(Employee, TechnicalSkills):
    """
    Represents a business analyst employee. Inherits from Employee and TechnicalSkills.

    Attributes:
        projects (list): A list of projects the business analyst is working on.
    """
    def __init__(self, name: str, id: str, salary: float, projects, certifications):
        """
        Initializes a BusinessAnalyst object.
        """
        Employee.__init__(self, name, id, salary)
        TechnicalSkills.__init__(self, certifications)
        self.projects = projects

    def work(self):
        """
        Returns a work description specific to a business analyst.
        """
        return f"{self.name} is analyzing requirements for projects: {', '.join(self.projects)}."

class CEO(Employee, ManagementSkills):
    """
    Represents a CEO employee. Inherits from Employee and ManagementSkills.

    Attributes:
        years_experience (int): The CEO's years of experience.
    """
    def __init__(self, name: str, id: str, salary: float, years_experience: int, leadership_level: int):
        """
        Initializes a CEO object.
        """
        Employee.__init__(self, name, id, salary)
        ManagementSkills.__init__(self, leadership_level)
        self.years_experience = years_experience

    def work(self):
        """
        Returns a work description specific to a CEO.
        """
        return f"{self.name} is strategizing for the company with {self.years_experience} years of experience."
    


ceo = CEO("John Doe", "123", 1000000, 20, 5)
print(ceo.work())
developer = BusinessAnalyst("Jane Smith", "456", 80000, ["Project A", "Project B"], ["Cert A", "Cert B"])
print(developer.work())
manager = Manager("Alice Johnson", "789", 90000, "HR", 4)
print(manager.work())
team_lead = TeamLead("Bob Brown", "101", 75000, 5, 3)
print(team_lead.work())


