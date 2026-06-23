class Car:
    def __init__(self, color, brand):       # initializer
        self.color = color
        self.brand = brand
        self.speed = 0
    
    # The __str__ magic method
    def __str__(self):                      #__str__ is a special method/dunder method
        return f"A beautiful {self.color} {self.brand} running at {self.speed} mph."

my_car = Car("Red", "Tesla")

# No more ugly memory address!
print(my_car)