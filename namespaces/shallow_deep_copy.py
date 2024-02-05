# = operator
l1=[1,2,3,4]
l2=l1
print(id(l1))
print(id(l2))
#refer to the same location in memory , so chang in one is reflected into another as well

# shallow copy --> copy()
l3=[1,2,3,4,5]
l4=l3.copy()
print(id(l3))
print(id(l4))
#refer to the different locations in memory

print(id(l3[1]))
print(id(l3[1]))
# it explains that , in shallow copy , two difference reference of list is created but reference of items is still same in shallow copy

# deep copy --> deepcopy()
import copy
l5=[1,2,3,4]
l6=copy.deepcopy(l5)
print(id(l5))
print(id(l6))
# lists now have different reference to their identifiers, just like in shallow copy

print(id(l5[1]))
print(id(l6[1]))

l7=[1,2,[3,4]]
l8=copy.deepcopy(l7)
print(id(l7))
print(id(l8))
print("=================")
print(id(l7[1]))
print(id(l8[1]))
print("=================")
print(id(l7[2][1]))
print(id(l8[2][1]))
print("=================")
l7[2][1]=1000
print(l7)
print(l8)
print(id(l7[1]))
print(id(l8[1]))
print(id(l7[2][1]))
print(id(l8[2][1]))

