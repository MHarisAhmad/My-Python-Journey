class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Mooo")

class Sheep:
    def speak(self):
        print("Ba")

animals = [Dog(), Cat(), Cow(), Sheep()]
for animal in animals:
    animal.speak()
