class car:
  def __init__(self,color,year):
    self.color = color
    self.year = year

  def start(self):
    print('the car has started....')
  def stop(self):
    print('the car has stopped...')

audi = car()
bmw = car()

print(audi.start(),bmw.stop())