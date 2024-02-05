# simple decorator
def decorator(func):
  a=2
  def wrapper():
    print("===========")
    nonlocal a
    a+=1
    print(a)
    func()
    print("===========")
  return wrapper

@decorator
def hello():
  print("nice")

hello()
# in it wrapper is able to access decorator function's variable a even after decorator function have done executing as it called for wrapper in it' return statement
# this is due to  CLOSURE ; that a inner function able to remember and use var. and all of it's outer function in which it is enclosed , inside it's local scope ; even after outer function is done with it's execution and is kind of out of frame now

"""o/p:
===========
3
nice
===========
"""
