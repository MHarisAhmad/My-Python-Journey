class Vehicle:
    def Start(self):
        return "Starting"
class Car(Vehicle):
    def drive(self):
        return "Driving"
car_01 = Car()
print(car_01.Start())
print(car_01.drive())
