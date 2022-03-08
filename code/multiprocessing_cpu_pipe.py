from multiprocessing import Process, Pipe

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

def worker(n, connection):
  with Timer(f'Process {n}'):
    result = do_work(n)
  connection.send(result)

def main():
  processes = []

  parent_connection, child_connection = Pipe()

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

    for n in range(MAX_REQUESTS):
      processes.append(Process(target=worker, args=(n,child_connection)))    
      
    for process in processes:
      process.start()
    
    for process in processes:
      results.append(parent_connection.recv()) # conn.recv is blocking!

  
  print(results)
      
if __name__ == '__main__':
  main()