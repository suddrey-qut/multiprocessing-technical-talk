import asyncio
import concurrent.futures

from timer import Timer
from util import do_work

MAX_REQUESTS = 10
ITERATIONS = 10000000

results = []

async def worker(n):
  with Timer(f'Process {n}'):
    result = do_work(n)
  return result

async def main():

  with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):
    for n in range(MAX_REQUESTS):
      future = worker(n)
      
      result = await future

      results.append(result)
      
  print(results)
      
if __name__ == '__main__':
  asyncio.run(main())