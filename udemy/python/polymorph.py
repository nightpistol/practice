#abstractbasemethods or interfaces

from abc import ABC,abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    return 'car has started'