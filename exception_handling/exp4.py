# doing both exception handling and decorator use
def divide(a,b):
    try:
        if isinstance(a,(int, float)) and isinstance(b,(int,float)):
            return a/b
        else:
            raise TypeError("Both parameters must be numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(e)

print(divide(2,3))
print(divide(2,0))
print(divide(True,'gj'))
