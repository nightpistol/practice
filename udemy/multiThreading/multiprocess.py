import multiprocessing
import time

def square_nums():
  for i in range(50):
    print(f"squares : {i**2}")

def cube_nums():
  for i in range(50):
    print(f"cubes : {i**3}")

#creating the process
if __name__ == '__main__':
  p1 = multiprocessing.Process(target=square_nums)
  p2 = multiprocessing.Process(target=cube_nums)

  t= time.time()

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  now = time.time()-t 
  print(now)       