# power of two generator

def gen5():
  a=-1
  while True:
    a+=1
    yield 2**a

a5=gen5()
for _ in range(5):
  print(next(a5))