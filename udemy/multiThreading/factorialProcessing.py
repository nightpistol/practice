import multiprocessing
import math
import time
import sys

#increasing max no of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute fact
def compute_fact(num):
  print(f"computing factorial of : {num}")
  result = math.factorial(num)
  return result

if __name__ == "__main__":
  numbers = [5000,6000,7000,8000]
  start_time = time.time()

  #creating pool of workers processes
  with multiprocessing.Pool() as pool:
    results = pool.map(compute_fact,numbers)

  end_time = time.time()  
  print(f"results:{results}")
  print(f"time taken : {end_time-start_time}")
