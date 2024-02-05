# builtin and global scope-namespace example
l=[1,2,3]
max(l) # of builtin scope output --> 3 # but in presence of def max, builtin is not searched for as we have max in global scope too: so consider  LEGB rule
def max(*args):
  print("hello")