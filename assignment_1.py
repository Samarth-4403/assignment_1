class Employee:
# Class defining objects with several attributes    
    def __init__(self, emp_no, name, salary, address, married):
        self.emp_no = emp_no
        self.name = name
        self.salary = salary
        self.address = address
        self.married = married

    def __str__(self):
        return (
            f"Employee No: {self.emp_no}\n"
            f"Employee Name: {self.name}\n"
            f"Employee Salary: {self.salary}\n"
            f"Employee Address: {self.address}\n"
            f"Employee Married: {self.married}"
        )

def get_employee_data():
# function prompts user for data and returns a new object with the input data
    emp_no = str(input("Enter Employee Number: ")) #changed input from int to str
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    address = input("Enter Employee Address: ")
    #changed from str to boolean 
    married = bool(input("Enter Employee Married (y/n): ").lower() in ("y", "yes"))
    return Employee(emp_no, name, salary, address, married)

def add_another_employee():
# function to add another employee
    response = input("Add another Employee (y/n): ")
    return response.lower() == "y"

def display_employees(employees):
# function that displays the details of each employee
    for employee in employees:
        print(employee)

def save_employees_to_csv(employees, filename):
    # Function to save the list of employee data to a CSV file
    with open(filename, "w", newline="") as csvfile:
        import csv  

        writer = csv.writer(csvfile)
        writer.writerow(["Employee No", "Name", "Salary", "Address", "Married"])  # Header row
        for employee in employees:
            writer.writerow(
                [
                    employee.emp_no,
                    employee.name,
                    employee.salary,
                    employee.address,
                    employee.married,
                ]
            )


if __name__ == "__main__":
    employees = []

    while True:  # Loop continuously until exit is chosen
        print("\nEmployee Management System")
        print("Press 1 to Add Employee")
        print("Press 2 to Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            new_employee = get_employee_data()
            employees.append(new_employee)
            print("\nEmployee added successfully!")
        elif choice == '2':
            print("\nExiting Employee Management System...\n")
            if employees:  # Save data only if there are employees
                save_employees_to_csv(employees, "employees.csv")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

    display_employees(employees)  # Display employees after exiting the loop
