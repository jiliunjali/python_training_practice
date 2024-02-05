"""
    print():
    it is a built-in function of python which is highly used, and since it is the part of tandard liberary of python. so , no explicit importing of any module is not required to use it.

    print(value,...,sep=' ',end='\n',file=sys.stout,flush=False)
    it is how print function is made in liberary , with various arguments
    value -> it is what is printed using print function; if it is not mentioned then sys.stout is printed by default
    file -> it is file-like stream which is by default sys.stout
    sep -> it is the argument which insert string in between each value and by default it is space
    end -> it is the argument which appends after last value and by default it is a newline
    flush -> it is related to whether to forcibly flushing the stream or not

    since print function have no return staement , so , it return -> None
"""
# different ways to use print fucntion
print("hello world") # output -> hello world
print('hello world') # output -> hello world

print("hello", "world") # output -> hello world

print("hello", "world", sep="/") # output -> hello/world

print("hello",55,sep="=",end=" ")
print("world", end=" yeh !!")
# output -> hello55 world yeh!!

# print statement with fstring
print()
f="here"
g="there"
print(f'{f} {g} where')
# output-> here there where

# representing that print function returns None
print(print(f)) # output -> None


