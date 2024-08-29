try:
  a = 4/0
except Exception as ex:
  print(ex)
finally:
  print('execution completed')  