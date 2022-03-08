from time import perf_counter

class Timer:
  def __init__(self, name):
    self.name = name

  def __enter__(self):
    self.start = perf_counter()
    return self

  def __exit__(self, *args):
    print('{}: {:.2f}s'.format(self.name, perf_counter() - self.start))