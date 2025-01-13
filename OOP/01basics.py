class Sample:
    def __init__(self,ssp):
        self.ssp =ssp
    def sp1(self):
        print( f'the name {self.ssp}')

sp = Sample('spot')
sp.sp1()

class calc:
    def add(self, a, b):
        return a + b
cl = calc()
print(cl.add(1,2))