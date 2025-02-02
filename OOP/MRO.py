#MRO: Method Resolution Order

# class A:
#     def disp(self):
#         print('class A')

# class B(A):
#     def disp(self):
#         print('class B')
#         super().disp()

# ob = B()
# ob.disp()
# print(B.__mro__)




class parent1:
    def show(self):
        print('parent class')

class parent2:
    def show(self):
        print('parent class')

class A(parent1):
    def show(self):
        print('class A')
        super().show()

class B(parent2):
    def show(self):
        print('class B')

class C(A,B):
    def show(self):
        print('class C')
        super().show()

ob = C()
ob.show()
print(C.__mro__)
