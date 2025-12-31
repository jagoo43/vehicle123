class BMW:
    def speed(self):
        print("BMW speed is 250 km/h")

    def fuel(self):
        print("BMW uses petrol")


class Ferrari:
    def speed(self):
        print("Ferrari speed is 320 km/h")

    def fuel(self):
        print("Ferrari uses petrol")


cars = [BMW(), Ferrari()]

for car in cars:
    car.speed()
    car.fuel()
