# factorial via recursion

def fac(num):
    if num ==1 or num==0:
        return 1
    else:
        return num*fac(num-1)

print(fac(5))