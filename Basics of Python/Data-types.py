"""
    datatypes of programming language can be simply aid to be types of data , the programming languauge can handle and work with.
    data types represent the type of value that a variable can hold.
    in python each variable holds data of specific type which is identified by interpreter dynamically.
    there are various types of datatypes in python:
"""
# Numeric Types:
    # int: Integer type represents whole numbers without any decimal points.
x = 5
print(type(x))

    # float: Float type represents numbers with decimal points.
y = 3.14
print(type(y))

    # complex: Complex type represents complex numbers with a real and imaginary part.
z = 2 + 3j
print(type(z))

# Text Type:
    # str: String type represents a sequence of characters enclosed in single or double quotes.
text = "it's lengthy"
print(type(text))

# Boolean Type:
# bool: Boolean type represents either True or False.
ist = True
isf = False
print(type(ist))

# Sequence Types:
    # list: List is an ordered and mutable sequence of elements.
L = [1, 2, 3, 'four', 5.0]
print(type(L))

    # tuple: Tuple is an ordered and immutable sequence of elements.
t = (1, 2, 3, 'four', 5.0)
print(type(t))

# Set Types:
    # set: Set is an unordered and mutable collection of unique elements.
s = {1, 2, 3, 4, 5}
print(type(s))
#being said that set stores the unique elements, means that it consider the repeated element only once
s1={1,2,2,2,3,4,5,6,1,7}
print(s1) # output -> {1, 2, 3, 4, 5, 6, 7}

# Mapping Type:
# dict: Dictionary is an unordered collection of key-value pairs.
d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(d))

# None Type:
# NoneType: Represents the absence of a value or a null value.
n = None
print(type(n))