#!/usr/bin/env python3

import requests

from multiprocessing import Process

from timer import Timer

MAX_REQUESTS = 10

resources = []

def worker(n):
  with Timer(f'Process {n}'):
    req = requests.get('https://www.cirrusrobotics.com.au', allow_redirects=True)
    resources.append(req.text)
    
processes = []

with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

  for n in range(MAX_REQUESTS):
    processes.append(Process(target=worker, args=(n,)))    
    
  for thread in processes:
    thread.start()

  for thread in processes:
    thread.join()
    


