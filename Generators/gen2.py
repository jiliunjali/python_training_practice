# generator for printing 8 odd perfect squares


def gen2():
    a=-1
    while True:
        a+=1
        if a**2 %2 != 0:
            yield a**2


a1= gen2()

for i in range(8):
    print(next(a1))

