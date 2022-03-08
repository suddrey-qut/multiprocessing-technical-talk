import concurrent.futures

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(n):
  with Timer(f'Process {n}'):
    result = do_work(n)
  return result

def main():
  futures = []

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):
    with concurrent.futures.ProcessPoolExecutor() as executor:
      for n in range(MAX_REQUESTS):
        futures.append(executor.submit(worker, n))

      for future in concurrent.futures.as_completed(futures):
         results.append(future.result())
        
      
  print(results)
      
if __name__ == '__main__':
  main()