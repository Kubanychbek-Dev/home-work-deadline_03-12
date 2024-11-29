class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheel):
        if wheel == 2:
            return f"Это мотоцикл марки {self.name}"
        elif wheel == 3:
            return f"Это трицикл марки {self.name}"
        elif wheel == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif 50001 < self.mileage < 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 < self.mileage < 150000:
            return f"{self.name} надо провести полную диагностику."
        elif self.mileage > 150000:
            return f"{self.name} лучше не покупать."


tesla = Vehicle("Tesla", 40000)
print(tesla.get_vehicle_type(4))
print(tesla.get_vehicle_advice())
print()

shevrolet = Vehicle("Shevrolet", 80001)
print(shevrolet.get_vehicle_type(4))
print(shevrolet.get_vehicle_advice())
print()

honda = Vehicle("Honda", 140008)
print(honda.get_vehicle_type(2))
print(honda.get_vehicle_advice())
print()

bmw = Vehicle("BMW", 180000)
print(bmw.get_vehicle_type(4))
print(bmw.get_vehicle_advice())