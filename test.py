# Base class
class Vehicle():
  def __init__(self):
    brand = "Ford"
  def honk(self):
    print("Tuut, tuut! \n")

# Derived class
class Car(Vehicle):
  def __init__(self):
    super().__init__()
    model = "Mustang"

myCar = Car()
myCar.honk()
print(f"{myCar.brand} {myCar.model}")