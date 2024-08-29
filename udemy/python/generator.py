def squares(n):
  for i in range(n):
    yield i**2
  
for i in squares(3):
  print(i)