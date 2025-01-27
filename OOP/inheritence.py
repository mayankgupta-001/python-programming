'single inheritence'

# class Parent:
#     def show(self):
#         print("This is a method in the Parent class.")

# class Child(Parent):
#     def display(self):
#         print("This is a method in the Child class.")

# # Create an instance of the Child class
# obj = Child()
# obj.show()     # Accessing the parent class method
# obj.display()  # Accessing the child class method




'multiple inheritence'

# class Parent1:
#     def method1(self):
#         print("This is method1 from Parent1.")

# class Parent2:
#     def method2(self):
#         print("This is method2 from Parent2.")

# class Child(Parent1, Parent2):
#     def method3(self):
#         print("This is method3 from Child.")

# # Create an instance of the Child class
# obj = Child()
# obj.method1()  # From Parent1
# obj.method2()  # From Parent2
# obj.method3()  # From Child




'multi-level inheritence'

# class Grandparent:
#     def method1(self):
#         print("This is a method from the Grandparent class.")

# class Parent(Grandparent):
#     def method2(self):
#         print("This is a method from the Parent class.")

# class Child(Parent):
#     def method3(self):
#         print("This is a method from the Child class.")

# # Create an instance of the Child class
# obj = Child()
# obj.method1()  # From Grandparent
# obj.method2()  # From Parent
# obj.method3()  # From Child




'hierarchical inheritence'

class Parent:
    def method1(self):
        print("This is a method in the Parent class.")

class Child1(Parent):
    def method2(self):
        print("This is a method in the Child1 class.")

class Child2(Parent):
    def method3(self):
        print("This is a method in the Child2 class.")

# Instances of Child1 and Child2
obj1 = Child1()
obj2 = Child2()

obj1.method1()  # From Parent
obj1.method2()  # From Child1

obj2.method1()  # From Parent
obj2.method3()  # From Child2