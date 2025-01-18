**Employee Management System**

This project demonstrates object-oriented programming concepts like inheritance and magic methods in Python by creating an Employee Management System with a graphical user interface (GUI).

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

* **Python:** Python 3.7 or later is required. You can download it from [python.org](https://www.python.org/).
* **Tkinter:** Tkinter is usually included with standard Python installations. If you encounter issues, you might need to install it separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu or `brew install python-tk@3.9` on macOS if using brew).

## Project Structure

The project consists of the following files:

* **employees_definitions.py:** This file contains the definitions for the `Employee` class hierarchy, including subclasses (Developer, TeamLead, Manager, BusinessAnalyst, CEO) and mixins (TechnicalSkills, ManagementSkills). You can also run this file directly to test the classes and their methods independently.
* **main_code.py:** This file contains the Tkinter GUI code that interacts with the employee classes defined in `employees_definitions.py`.

## Running the Application

1. **Save the files:** Save both `employees_definitions.py` and `main_code.py` in the same directory.

2. **Open a terminal or command prompt:** Navigate to the directory where you saved the files using the `cd` command. For example:

   ```bash
   cd /path/to/your/project/directory
   ```

### Running Tests in `employees_definitions.py` (Optional)

1. **To test the classes and methods defined in `employees_definitions.py` directly:**

   ```bash
   python employees_definitions.py
   ```

   This might not produce any visual output but will execute the code in the file, allowing you to test the functionality of the classes.

### Running the GUI Application in `main_code.py`

1. **To run the Employee Management System GUI application:**

   ```bash
   python main_code.py
   ```

   This will launch the graphical user interface where you can interact with the employee data.

## Using the Application

   *   **Adding Employees:**
       *   Enter the employee's name, ID, and salary in the respective input fields.
       *   Select the employee's role from the "Role" dropdown menu.
       *   Depending on the selected role, additional input fields will appear in the "Additional Information" section. Fill in these fields as appropriate.
       *   Click the "Add Employee" button to add the employee to the system. The employee will be displayed in the employee list below.
   *   **Comparing Salaries:**
       *   Select exactly two employees from the employee list by clicking on their rows.
       *   Click the "Compare Selected Salaries" button. A message box will appear, showing which employee has a higher salary or if they have the same salary.

## Understanding the Code (Focus on Object-Oriented Concepts)

The code demonstrates the following object-oriented programming (OOP) concepts:

* **Inheritance:** Subclasses like `Developer`, `TeamLead`, etc., inherit attributes and methods from the base `Employee` class. This promotes code reuse and creates a clear hierarchy.
* **Mixins:** The `TechnicalSkills` and `ManagementSkills` classes are mixins. They provide additional capabilities to classes that inherit from them. This allows you to add specific skills to different employee types without creating complex inheritance hierarchies.
* **Magic Methods:** Special methods like `__init__` (constructor), `__str__` (string representation), `__repr__` (representation), `__lt__` (less than), and `__gt__` (greater than) define how objects are created, represented as strings, and compared.

By running and experimenting with this application, you can gain a practical understanding of these important OOP concepts.