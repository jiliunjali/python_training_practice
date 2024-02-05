# timing decorator as method decorator
import time

class sample:

  # def __init__(self):
  #   self.answer=None

  def calculating(num_arg):
    def time_decorator(func):
      def wrapper(*args):
        if num_arg+1 == len(args):
          start=time.time()
          result =func(*args)
          print(f"time taken to execute {func.__name__} is ",time.time()-start)
          return 'result is '+ str(result)
        else:
          raise ValueError("number of inputs provided is incorrect")
      return wrapper
    return time_decorator

  @calculating(2)
  def expo(self,a,b):
    return a**b


  @calculating(1)
  def square(self,a):
    return a**2

sam=sample()
print(sam.expo(2,3))
print(sam.square(4))


