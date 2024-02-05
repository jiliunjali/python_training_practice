# multiple exception handling
try:
    # Open the file in write mode
    f = open('sample.txt', 'w')
    f.write('a r rahman')
    f.close()

    # Open the file in read mode
    f1 = open('sample.txt', 'r')
    print(f1.read())

except FileNotFoundError:
    print('There is no such file')

except Exception as e:
    print("***************")
    print(e)
