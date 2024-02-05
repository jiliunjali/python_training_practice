# generators for fibonnacii series

def gen1():
  a=0
  b=1
  while True:
    yield a
    a,b=b, a+b
num=10
a=gen1()
for _ in range(num+1):
  print(next(a))
