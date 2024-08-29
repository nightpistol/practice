# multithreading and threadpool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_num(number):
  time.sleep(1)
  return f"number: {number}"

numbers =[1,2,3,4,5,6]
with ThreadPoolExecutor(max_workers=3) as executor:
  results = executor.map(print_num,numbers)

for result in results:
  print(result)  