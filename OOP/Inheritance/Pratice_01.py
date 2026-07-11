class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return f"{self.name} makes sound"
class Dog(Animal):
    bark = "woff woff woff"


dog = Dog("Jacky")
print(dog.bark)
print(dog.name)
