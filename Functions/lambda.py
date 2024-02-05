# practicing lambda function

l1=[1,2,3,4,5,6,7,8,9]
le=list(filter(lambda l : l%2==0,l1))
lo=list((x**2 for x in filter(lambda l : l%2 !=0,l1)))
print(l1)
print(list(set(l1)-set(le)))
print(lo)

loo=list(x**2 for x in set(l1)-set(le))
loo