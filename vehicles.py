class Vehicle:
    def __init__(self, vehiclename, vehiclemodel):
        self.vehiclename = vehiclename
        self.vehiclemodel = vehiclemodel

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")

class Firstcar(Vehicle):
    def display(self):
        print(f"The first car was {self.vehiclename}. It was a {self.vehiclemodel}.")

class Motorcycle(Vehicle):
    def __init__(self, vehiclename, vehiclemodel, cc):
        super().__init__(vehiclename, vehiclemodel)
        self.cc = cc

    def display(self):
        print(
            f"The first motorcycle is {self.vehiclename}  {self.vehiclemodel}. { self.cc} cc")


car = Firstcar("Toyota", "Premio")
car.display()
car = Motorcycle ("Kawasaki", "Ninja", 2000)
car.display()

