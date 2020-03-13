class Car:
    def __init__(self, num):
        self.door = Door(1)
        self.wheel = Wheel(1)

class Door:
    def __init__(self, num):
        self.number = num

class Wheel:
    def __init__(self, num):
        self.number = num

class Taxi(Car):
    def __init__(self):
        super();
        self.color = "red"