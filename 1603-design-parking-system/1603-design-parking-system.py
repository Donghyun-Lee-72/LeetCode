class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.lot[carType - 1] == 0:
            return False
        else:
            self.lot[carType - 1] -= 1
            return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)