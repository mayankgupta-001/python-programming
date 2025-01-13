class Employee:
  def __init__(self, name, emp_id, deptt, salary):
    self.name = name
    self.emp_id = emp_id
    self.deptt = deptt
    self.salary = salary

  def display(self):
    emp = f'''
    Name: {self.name}
    dep: {self.deptt}
    salary:{self.salary}
    empid:{self.emp_id}'''
    print(emp)

  def update_info(self,name=None, deptt=None, salary=None):
    if name:
      self.name = name
    if deptt:
      self.deptt = deptt
    if salary:
      self.salary = salary
      
  def increment(self,inc):
    self.salary = self.salary + (self.salary * inc/100)



class Employee_management(Employee):
  def __init__(self):
    self.reg = {}

  def add_employee(self,name,emp_id,deptt,salary):
    self.reg[emp_id] = Employee(name,emp_id,deptt,salary)

  def display_all(self):
    for emp in self.reg:
      self.reg[emp].display()

  def incrementt(self,emp_id,inc):
    if emp_id not in self.reg:
      print("Employee not found")
    else:
      self.reg[emp_id].increment(inc)
    




#main code
system = Employee_management()
system.add_employee('Shiva',15,'cse',20000)
system.add_employee('Ram',16,'cse',200000)
system.display_all()

system.incrementt(15,10)
system.display_all()
    

#main
# emp1 = Employee('Ram',12,'cse',12000)
# emp1.display()

# emp1.update_info(name='raj')
# emp1.display()

# emp1.increment(10)
# emp1.display()