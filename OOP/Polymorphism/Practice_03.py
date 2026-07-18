class Person:
    def greet(self):
        print("Hello")
class Robot:
    def greet(self):
        print("Greetings")

def say_hello(obj):
    obj.greet()

say_hello(Person())
say_hello(Robot())