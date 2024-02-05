# even fibonacci generator

def gen4():
    a,b=0,1
    while True:
        if a%2==0:
            yield a
        a,b=b, a+b

a4=gen4()
for _ in range(6):
    print(next(a4))