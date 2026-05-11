
# 2-m
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start_engine(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")

class Simple:
    def test(self):
        print("Oddiy method")

class Driver:
    def drive(self, car_obj):
        if hasattr(car_obj, "start_engine"):
            car_obj.start_engine
        else:
            print("start_engine topilmadi")

c1 = Car("BMW", 220)
s1 = Simple

driver = Driver()

driver.drive(c1)
print("--------------")
driver.drive(s1)
