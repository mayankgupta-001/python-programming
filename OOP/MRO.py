#MRO: Method Resolution Order

class A:
    def show(self):
        print('class A')

class B:
    def show(self):
        print('class B')

class C(A,B):
    def show(self):
        pass
ob = C()
ob.show()