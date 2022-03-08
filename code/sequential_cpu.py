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
  with Timer(f'Total time taken to perform {MAX_REQUESTS} jobs'):
    for n in range(MAX_REQUESTS):
      worker(n)  
      
  print(results)  

if __name__ == '__main__':
  main()