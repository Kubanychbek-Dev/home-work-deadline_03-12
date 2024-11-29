class Car:
    def __init__(self, model, types, color):
        self.model = model
        self.types = types
        self.color = color

    def to_drive(self):
        return f"You driving a {self.color} {self.model} {self.types} car"

    def to_buy(self):
        return f"Do you want to buy a {self.color} {self.model} {self.types} car?"


my_mersedes = Car("Mersedes", "crossover", "white")
print(my_mersedes.to_drive())
print()

shevrolet = Car("Chevrolet Tahoe", "SUV", "Black")
print(shevrolet.to_buy())