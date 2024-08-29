class car:
  def __init__(self,color,year,engine):
    self.color = color
    self.year = year
    self.engine = engine

  def start(self):
    print('the car has started....')
  def stop(self):
    print('the car has stopped...')

class vehicle:
  def __init__(self,pollution,permission):
    self.pollution = pollution
    self.permission = permission     

class tesla(car,vehicle):
  def __init__(self,color,year,engine,pollution,permission,model):
     car.__init__(self,color,year,engine)
     vehicle.__init__(self,pollution,permission)
     self.model = model

  def selfDrive(self):
    print('it supports self driving') 

modelS = tesla('red',2024,'electric','free','yes','S')
modelS.start() 
modelS.selfDrive()     
print(modelS.color)