# Base class
class Vehicle():
  def __init__(self):
    brand = "BMW"
  def honk(self):
    print("Doot, doot! \n")

# Derived class
class Car(Vehicle):
  def __init__(self):
    super().__init__()
    model = "X6"

myCar = Car()
myCar.honk()
print(f"{myCar.brand} {myCar.model}")