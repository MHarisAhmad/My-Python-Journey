class Bird:
    def move(self):
        return "Flying"
class Penguin(Bird):
    def move(self):
        return "Swimming"
bird_01 = Penguin()
print(bird_01.move())