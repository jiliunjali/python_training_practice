# geenrator question for practicing printing even number
# # normal approach
# num = 10000
# for i in range(num+1):
#   if i%2==0:
#     print(i)

# # using generator
# def gen(num):
#   for i in range(num):
#     if i%2==0:
#       yield i

# a=gen(num)
# for i in a:
#   print (i)

#comaparing them via decorator

import time
#from memory_profiler import profile
import psutil # for memory


def timer(func):
    def wrapper(*args):
        start = time.time()
        result=func(*args)
        memory_info = psutil.Process().memory_info()
        print(f"Memory used: {memory_info.rss / (1024 * 1024):.2f} MB")
        print(f"for function {func.__name__} , time taken is ",time.time()-start)
        return result
    return wrapper

@timer
def normal(num):
    for i in range(num+1):
        if i%2==0:
            print(i)

@timer
def gen(num):
    for i in range(num):
        if i%2==0:
            yield i

num=10
normal(num)
a=gen(num)
for i in a:
    print(i)




