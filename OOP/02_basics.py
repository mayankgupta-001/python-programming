# class student:
#     count = 0
# o1 = student()
# o2 = student()
# o1.count = 20
# print(o1.count)



class student:
    count = 0
    def __init__(self, name, rolln):
        self.name = name
        self.rolln = rolln
        student.count += 1
    
    @classmethod
    def get_count(cls):
        return f'student count: {cls.count}'



s1 = student('Raj',1)
s2 = student('Suraj',2)
print(s1.get_count())
print(s2.count)