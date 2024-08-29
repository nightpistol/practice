# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

#   #dunder method overriding
#   def __str__(self):
#     return f"{self.name} , {self.age} years old"  

# me = Person('saqlain',43)    
# print(me)

class Vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __add__(self,other):
    return Vector(self.x+other.x,self.y+other.y)
  
  def __repr__(self):
    return f"vector({self.x},{self.y})"

v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1+v2)