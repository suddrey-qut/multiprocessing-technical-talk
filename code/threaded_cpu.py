from threading import Thread

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(n):
  with Timer(f'Thread {n}'):
    result = do_work(n)
  results.append(result)

def main():
  threads = []

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

    for n in range(MAX_REQUESTS):
      threads.append(Thread(target=worker, args=(n,)))    
      
    for thread in threads:
      thread.start()

    for thread in threads:
      thread.join()
      
  print(results)


if __name__ == '__main__':
  main()