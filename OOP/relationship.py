# Super class or Base class or Parent class

# 'is-A relationship'

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def sound(self):
#         return 'Genric Sound'
    
# # Subclass or Child class

# class Cat(Animal):
#     def sound(self):
#         return f'{self.name} sounds Meow...'

# o = Cat('Kitty')
# print(o.sound())






'Component class'
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f'''
Name: {self.name}
Employee Id: {self.emp_id}
Salary: {self.salary}''')
        
# emp1 = Employee('Raghav', 'gla124', 12500)
# emp1.display_info()




'Container class'
class Management:
    def __init__(self, emp):
        self.emp = emp  # Has-A Relationship

emp1 = Employee('Raghav', 'gla124', 12500)
system = Management(emp1)
system.emp.display_info()