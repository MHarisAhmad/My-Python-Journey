class Employee:
    def __init__(self):
        pass
    def work(self):
        return "Wroking"
class Manager(Employee):
    pass
class Developer(Employee):
    pass
class Designer(Employee):
    pass

p1 = Manager()
p2 = Developer()
p3 = Designer()
print(p1.work())
print(p2.work())
print(p3.work())