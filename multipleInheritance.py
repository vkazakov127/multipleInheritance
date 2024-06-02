class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self):
        return 300


class Nissan(Vehicle, Car):
    price = 2000000
    vehicle_type = 'SUV'

    def horse_powers(self):
        return 600


Nissan1 = Nissan()
print(f'Nissan1.vehicle_type = {Nissan1.vehicle_type}, Nissan1.price = {Nissan1.price}')