import threading
import time

def print_nums():
  for i in range(5):
    print(f"number: {i}")

def print_letters():
  for letter in "abcde":
    print(f"letter: {letter}")

#creating two threads
t1 = threading.Thread(target=print_nums)
t2 = threading.Thread(target=print_letters)

t=time.time()
#starting the threads
t1.start()
t2.start()

#wait for threads to end and join main thread
t1.join()
t2.join()

finishTime = time.time()-t 
print(finishTime)       