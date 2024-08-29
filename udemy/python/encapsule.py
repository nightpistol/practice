class Person:
  def __init__(self,name,age):
    self.__name = name   #private variables
    self.__age = age

# getter method
  def get_name(self):
    return self.__name

#setter method
  def set_name(self,name):
    self.__name = name  

saq = Person('saqlain',24)
print(saq.get_name())
saq.set_name('musthak')
print(saq.get_name())    