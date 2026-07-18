class Battery:
    def charge(self):
        print("charging")
class Phone:
    def __init__(self):
        self.battery = Battery()
Phone().battery.charge()


#-------------------------------------

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

Car().engine.start()