import json
from Checkpoint1 import Employee

class EmployeeManager:
    """ 
    Manages employee records (CRUD operations).
    
    Attributes:
        employees (list): List of employee records.
    """
    FILE_NAME = "Current_Employees.json"

    def __init__(self):
        """Initializes the manager and loads existing employees."""
        self.employees = self.load_employees()
        if not self.employees:
            self.initialize_default_employees()

    def load_employees(self):
        """Loads employees from the JSON file."""
        try:
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"{self.FILE_NAME} not found. Initializing default records.")
        except json.JSONDecodeError:
            print(f"Error reading {self.FILE_NAME}. Starting fresh.")
        return []

    def save_employees(self):
        """Saves current employee records to the JSON file."""
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(self.employees, file, indent=4)
        except IOError:
            print("Error saving to file. Please check permissions.")

    def initialize_default_employees(self):
        """Populates the system with default employees if empty."""
        defaults = [
            Employee("Alice Johnson", 30, "Software Engineer", 80000, "IT", "New York"),
            Employee("Bob Smith", 40, "Project Manager", 95000, "Management", "San Francisco"),
            Employee("Charlie Brown", 28, "Data Analyst", 70000, "Finance", "Chicago"),
            Employee("Diana Prince", 35, "HR Specialist", 65000, "Human Resources", "Seattle")
        ]
        self.employees = [emp.to_dict() for emp in defaults]
        self.save_employees()

    def add_employee(self):
        """Adds a new employee via user input."""
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            department = input("Enter department: ")
            location = input("Enter location: ")
        except ValueError:
            print("Invalid input! Age must be an integer and salary must be a number.")
            return

        # Check for duplicate employee
        if any(emp["name"].lower() == name.lower() and emp["position"].lower() == position.lower() for emp in self.employees):
            print("Error: Employee with the same name and position already exists.")
            return

        new_employee = Employee(name, age, position, salary, department, location)
        self.employees.append(new_employee.to_dict())
        self.save_employees()
        print(f"Employee '{name}' added successfully!")

    def view_employees(self):
        """Displays all employees."""
        if not self.employees:
            print("No employees found.")
            return

        print("\nList of Employees:")
        for emp in self.employees:
            print(emp)
