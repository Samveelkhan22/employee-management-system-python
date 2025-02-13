import json

class Employee:
    """ 
    Represents an employee.
    
    Attributes:
        name (str): Employee's name.
        age (int): Employee's age.
        position (str): Employee's position.
        salary (float): Employee's salary.
        department (str): Department name.
        location (str): Location name.
    """
    def __init__(self, name, age, position, salary, department, location):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary
        self.department = department
        self.location = location
    
    # Getters and Setters
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self._salary = salary

    def to_dict(self):
        """Converts the Employee object into a dictionary."""
        return {
            "name": self._name,
            "age": self._age,
            "position": self._position,
            "salary": self._salary,
            "department": self.department,
            "location": self.location
        }

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
        """Loads employees from the JSON file.
        
        Returns:
            list: Employee records or empty list if file not found.
        """
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

    def update_employee(self):
        """Updates an existing employee's information."""
        name = input("Enter employee name to update: ")
        for emp in self.employees:
            if emp["name"].lower() == name.lower():
                print("Enter new details (press Enter to skip):")
                emp["age"] = int(input("New age: ") or emp["age"])
                emp["position"] = input("New position: ") or emp["position"]
                emp["salary"] = float(input("New salary: ") or emp["salary"])
                emp["department"] = input("New department: ") or emp["department"]
                emp["location"] = input("New location: ") or emp["location"]
                self.save_employees()
                print(f"Employee '{name}' updated successfully!")
                return
        print(f"Employee '{name}' not found.")

    def delete_employee(self):
        """Deletes an employee by name."""
        name = input("Enter employee name to delete: ")
        original_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp["name"].lower() != name.lower()]
        
        if len(self.employees) < original_count:
            self.save_employees()
            print(f"Employee '{name}' deleted successfully.")
        else:
            print(f"Employee '{name}' not found.")

    def search_employee(self):
        """Searches for employees by name."""
        name = input("Enter employee name to search: ")
        matches = [emp for emp in self.employees if name.lower() in emp["name"].lower()]

        if matches:
            print("\nMatching Employees:")
            for emp in matches:
                print(emp)
        else:
            print("No matching employees found.")

    def sort_employees(self):
        """Sorts employees based on salary or position."""
        criterion = input("Sort by salary or position? (salary/position): ").lower()

        if criterion == "salary":
            self.employees.sort(key=lambda x: x["salary"], reverse=True)
        elif criterion == "position":
            self.employees.sort(key=lambda x: x["position"].lower())
        else:
            print("Invalid sorting criterion. Use 'salary' or 'position'.")
            return

        self.save_employees()
        self.view_employees()

# Main Program
def main():
    """Displays the menu and handles user actions."""
    manager = EmployeeManager()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Sort Employees")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_employees()
        elif choice == "3":
            manager.update_employee()
        elif choice == "4":
            manager.delete_employee()
        elif choice == "5":
            manager.search_employee()
        elif choice == "6":
            manager.sort_employees()
        elif choice == "7":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
