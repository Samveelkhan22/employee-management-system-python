def update_employee(self):
        """Updates an existing employee's information."""
        name = input("Enter employee name to update: ")
        for emp in self.employees:
            if emp["name"].lower() == name.lower():
                print("Enter new details (press Enter to skip):")
                try:
                    emp["age"] = int(input("New age: ") or emp["age"])
                    emp["position"] = input("New position: ") or emp["position"]
                    emp["salary"] = float(input("New salary: ") or emp["salary"])
                except ValueError:
                    print("Invalid input! Age must be an integer and salary must be a number.")
                    return

                emp["department"] = input("New department: ") or emp["department"]
                emp["location"] = input("New location: ") or emp["location"]
                self.save_employees()
                print(f"Employee '{name}' updated successfully!")
                return
        print(f"Employee '{name}' not found.")
