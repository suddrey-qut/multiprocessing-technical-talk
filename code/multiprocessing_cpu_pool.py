from multiprocessing import Pool

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(o):
  with Timer(f'Process {o.n}'):
    result = do_work(o.n)
  return result

class Test:
  def __init__(self, n):
    self.n = n

def main():

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):
    with Pool(processes=16) as pool:
      results = pool.map(worker, [Test(1), Test(2), Test(3), Test(4), Test(5)])
      
  print(results)
      
if __name__ == '__main__':
  main()