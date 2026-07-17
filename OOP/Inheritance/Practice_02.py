class Phone:
    def __init__(self):
        pass
    def brand(self):
        return "Iphone"
class smartphone(Phone):
    pass

phone_01 = smartphone()
print(phone_01.brand())