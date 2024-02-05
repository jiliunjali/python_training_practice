# for understanding how raise works wihtout try and catch
def do(x,y):
    if y == 0:
        raise ZeroDivisionError("enter anything but zero") # stack trace with our message is output
    else:
        return x/y

# do(4,0)
do(9,4)