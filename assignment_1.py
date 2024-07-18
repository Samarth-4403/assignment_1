class Employee:
# Class defining objects with several attributes    
    def __init__(self, emp_no, name, salary, address, married):
        self.emp_no = emp_no
        self.name = name
        self.salary = salary
        self.address = address
        self.married = married

    def __str__(self):
        return f"Employee No: {self.emp_no}\nEmployee Name: {self.name}\nEmployee Salary: {self.salary}\nEmployee Address: {self.address}\nEmployee Married: {self.married}"

def get_employee_data():
# function prompts user for data and returns a new object with the input data
    emp_no = int(input("Enter Employee Number: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    address = input("Enter Employee Address: ")
    married = input("Enter Employee Married (True/False): ") == "True"
    return Employee(emp_no, name, salary, address, married)

def add_another_employee():
# function to add another employee
    response = input("Add another Employee (y/n): ")
    return response.lower() == "y"

def display_employees(employees):
# function that displays the details of each employee
    for employee in employees:
        print(employee)

def save_employees_to_file(employees, filename):
# function to save the list of employee data to a text file
    with open(filename, "w") as f:
        for employee in employees:
            f.write(str(employee) + "\n")

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
                save_employees_to_file(employees, "employees.txt")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

    display_employees(employees)  # Display employees after exiting the loop
