# for practicing assert statement

def tell_even(num):
    assert num % 2 == 0 , "can't you even enter a even ? " #stack trace with our message is output
    return " yes , it's even you know maths"

number = int(input("you are good at maths ? then enter a 3 digit even number : "))
tell_even(number)