class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

#---------------------------

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

def move(Vehicle):
    Vehicle.move()

move(Car())
move(Plane())