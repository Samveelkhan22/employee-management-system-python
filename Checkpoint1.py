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
