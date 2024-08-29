from abc import ABC,abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    print('vehicle has staretd') 

audi = Car()
audi.start()     