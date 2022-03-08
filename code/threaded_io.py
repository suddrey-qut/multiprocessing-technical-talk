#!/usr/bin/env python3
import requests
from threading import Thread

from timer import Timer

MAX_REQUESTS = 10

resources = []

def worker(n):
  with Timer(f'Thread {n}'):
    req = requests.get('https://www.cirrusrobotics.com.au', allow_redirects=True)
    resources.append(req.text)
    
threads = []

with Timer(f'Time taken to complete {MAX_REQUESTS} jobs'):

  for n in range(MAX_REQUESTS):
    threads.append(Thread(target=worker, args=(n,)))    
    
  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()
    


