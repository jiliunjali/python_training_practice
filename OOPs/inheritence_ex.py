# inheritance
class Vehicle:
  def __init__(self,make,model,year):
    self.make=make
    self.model=model
    self.year=year

  def display_info(self):
    print (f"this vechile is made by {self.make} with a given model: {self.model} in year {self.year}")

class Car(Vehicle):
  pass

class Motorcycle(Vehicle):
  pass

c=Car('honda','sfd','3456')
m=Motorcycle('pulsar','fvv',664)
c.display_info()
m.display_info()
type(c)
