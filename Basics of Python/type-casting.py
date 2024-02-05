"""
    Type casting, also known as type conversion, is the process of converting a variable from one data type to another.
    there are 2 types of type casting :
    1) implicit type casting: Python automatically performs type conversion when it is required.
    2) explicit type casting: type conversion that programmer especially specifies.

"""

# implicit type casting : it is done intelligently by python when performing operations between different data types.
x = 5        # int
y = 2.0      # float
result = x + y  # int + float -> float
print(result)   # Output: 7.0

# explicit type casting : it is done by programmer by using predefined functions, to convert datatype of variable or value into another.
f = 7.8
i = int(f)
print(i)  # Output: 7

""" 
there are various perdefined functions to perform type casting for each datatype.
"""
# int() -> for int conversion
s ='45'
print(4+int(s)) # s is converted into a integer
f1=4.55
print(int(f1)) # output -> 4

# str() -> string conversion
num = 10
num_str = str(num)
print(num_str)  # Output-> '10'

# list(), set(), tuple() -> for their conversions to those datatypes.
g = "hello"
list1 = list(g)
print(list1)  # Output-> ['h', 'e', 'l', 'l', 'o']
