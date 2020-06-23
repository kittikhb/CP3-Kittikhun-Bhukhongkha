class Vehicle():
    licensePlate =""
    RegisteredName =""
    carModel=""
    def turnOnAC(self):
        print(self.carModel,"AC turned on")

class PickUpCar(Vehicle):
    pass
class Van(Vehicle):
    pass
class Sedan(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

pickup1 = PickUpCar()
van1 = Van()
sedan1 = Sedan()
estateCar1 = EstateCar()

pickup1.carModel = "Pick Up"
van1.carModel = "Van"
sedan1.carModel = "Sedan"
estateCar1.carModel = "Estate Car"

pickup1.turnOnAC()
van1.turnOnAC()
sedan1.turnOnAC()
estateCar1.turnOnAC()
