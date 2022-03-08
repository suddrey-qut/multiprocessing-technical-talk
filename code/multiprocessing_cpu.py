from multiprocessing import Process

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(n):
  with Timer(f'Process {n}'):
    result = do_work(n)
  results.append(result)

def main():
  processes = []

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

    for n in range(MAX_REQUESTS):
      processes.append(Process(target=worker, args=(n,)))    
      
    for process in processes:
      process.start()

    for process in processes:
      process.join()

    
  print(results)
      
if __name__ == '__main__':
  main()