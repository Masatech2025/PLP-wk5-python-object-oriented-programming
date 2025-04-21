class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

def demonstrate_movement(vehicle):
    vehicle.move()

my_car = Car()  # Fix: Use Car() with a capital 'C'
my_plane = Plane()
my_bicycle = Bicycle()

demonstrate_movement(my_car)
demonstrate_movement(my_plane)
demonstrate_movement(my_bicycle)
