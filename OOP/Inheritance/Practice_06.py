#----------------------
#WAY 01

class Person:
    def introduce(self):
        print("Hello")
class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student")
person_01 = Student()
person_01.introduce()

#--------------------------------------
#WAY 02

class Person:
    def introduce(self):
        return "Hello"
class Student(Person):
    def introduce(self):
        super().introduce() + "\nI am a student"
        
person_01 = Student()
person_01.introduce()