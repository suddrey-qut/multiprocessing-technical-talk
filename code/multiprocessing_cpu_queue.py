from multiprocessing import Process, Queue

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(n, queue):
  with Timer(f'Process {n}'):
    result = do_work(n)
  queue.put(result)

def main():
  processes = []

  queue = Queue()

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

    for n in range(MAX_REQUESTS):
      processes.append(Process(target=worker, args=(n,queue)))    
      
    for process in processes:
      process.start()
    
    for process in processes:
      results.append(queue.get()) # queue.get is blocking!

  
  print(results)
      
if __name__ == '__main__':
  main()