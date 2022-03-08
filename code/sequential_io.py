#!/usr/bin/env python3

import requests

from timer import Timer

MAX_REQUESTS = 10

result = []

def worker(n):
  with Timer(f'Request {n}'):
    req = requests.get('https://www.cirrusrobotics.com.au', allow_redirects=True)
    result.append(req.text)

def main():
  with Timer(f'Total time taken to perform {MAX_REQUESTS} requests'):
    for n in range(MAX_REQUESTS):
      worker(n)
    
if __name__ == '__main__':
  main()


