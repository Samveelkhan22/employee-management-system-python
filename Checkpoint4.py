from Checkpoint2 import EmployeeManager

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
