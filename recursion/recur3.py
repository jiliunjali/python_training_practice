# normal recursion example
def hel(num):
  if num == 1:
    print("hello")
  else:
    print("hello")
    return hel(num-1)

hel(5)