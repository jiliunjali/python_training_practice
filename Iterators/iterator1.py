#custom iterator
class Countdown:
  def __init__(self,n):
    self.n=n
    self.current =n+1

  def __iter__(self):
    return self

  def __next__(self):
    if self.current <= 1:
      raise StopIteration
    else:
      self.current-=1
      return self.current


count = Countdown(5)

for i in count:
  print(i)