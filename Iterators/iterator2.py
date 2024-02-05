# custom iterator on fibbonacii

class iter_obj:
  def __init__(self, num):
    self.num=num
    self.a=0
    self.b=1
    self.current=0 # to keep track of iterations

  def __iter__(self):
    return fibiter(self)

class fibiter:
  def __init__(self,iobj):
    self.iobj = iobj

  def __iter__(self):
    return self

  def __next__(self):
    if self.iobj.current < self.iobj.num:
      result =self.iobj.a
      self.iobj.a, self.iobj.b = self.iobj.b, self.iobj.a + self.iobj.b
      self.iobj.current+=1
      return result
    else:
      raise StopIteration



number =5
i=iter_obj(5)
it=fibiter(i)

for value in it:
  print(value)
