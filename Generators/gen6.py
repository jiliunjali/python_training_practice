def gen7(n):
  for i in range(1,n+1):
    yield i**2

num=5
a=gen7(num)

for i in range(num):
  print(next(a))