class Employee:
    def __init__(self, name, emp_id, deptt, salary):
        self.name = name
        self.emp_id = emp_id
        self.deptt = deptt
        self.salary = salary

    def display_info(self):
        emp = f'''Name: {self.name}
dep: {self.deptt}
salary: ${self.salary}
empid: {self.emp_id}'''
        print('\nEmployees Details')
        print(emp)

    def update_info(self, name=None, deptt=None, salary=None):
        if name:
            self.name = name
        if deptt:
            self.deptt = deptt
        if salary:
            self.salary = salary

    def increment(self, inc):
        self.salary = self.salary + (self.salary * inc / 100)


class Employee_management(Employee):
    def __init__(self):
        self.reg = {}

    def add_employee(self, name, emp_id, deptt, salary):
        self.reg[emp_id] = Employee(name, emp_id, deptt, salary)

    def display_all(self):
        for emp in self.reg:
            self.reg[emp].display_info()

    def incrementt(self, emp_id, inc):
        if emp_id not in self.reg:
            print("Employee not found")
        else:
            self.reg[emp_id].increment(inc)

    def delete_employee(self, emp_id):
        if emp_id in self.reg:
            del self.reg[emp_id]
            print(f"Employee with ID {emp_id} deleted.")
        else:
            print("Employee not found.")

    def update_employee_by_id(self, emp_id, name=None, deptt=None, salary=None):
        if emp_id in self.reg:
            self.reg[emp_id].update_info(name, deptt, salary)
            print(f"Employee with ID {emp_id} updated.")
        else:
            print("Employee not found.")


# Main code
system = Employee_management()
while True:
    print('\n 1.Add Employee \n 2. Update Employee details \n 3. Display All Employees \n 4. Salary increment by ID \n 5. delete the employee by id \n 6. Exit ')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Employee name: ')
        emp_id = input('Enter employee id: ')
        deptt = input('Enter employee department: ')
        salary = int(input('Enter employee salary: '))
        system.add_employee(name, emp_id, deptt, salary)

    elif choice == 2:
        emp_id = input('Enter employee id: ')
        name = input('Enter new Employee name (or leave blank): ')
        deptt = input('Enter new employee department (or leave blank): ')
        salary = input('Enter new employee salary (or leave blank): ')
        salary = int(salary)
        system.update_employee_by_id(emp_id, name, deptt, salary)

    elif choice == 3:
        system.display_all()

    elif choice == 4:
        emp_id = input('Enter employee id: ')
        inc = float(input('Enter the increment: '))
        system.incrementt(emp_id, inc)

    elif choice == 5:
        emp_id = input('Enter employee id: ')
        system.delete_employee(emp_id)

    elif choice == 6:
        break

#main code
# system = Employee_management()
# system.add_employee('Shiva',15,'cse',20000)
# system.add_employee('Ram',16,'cse',200000)
# system.display_all()

# system.incrementt(15,10)
# system.display_all()
    

#main
# emp1 = Employee('Ram',12,'cse',12000)
# emp1.display_info()

# emp1.update_info(name='raj')
# emp1.display_info()

# emp1.increment(10)
# emp1.display_info()