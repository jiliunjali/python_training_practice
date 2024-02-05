"""
    Variables :
    in programming languages , Variables are generally set to be a containers where we stored anything for the future use or reference .
    for example:If we want to make a homepage and there we want to display 'hello user_name' depending upon which user is accessing the home page .
    We might not necessarily know which One of the user is accessing the page at the moment .
    so what we can do is , attach 'hello' with a variable user_name where we will store the name of the user whoever is logging in.
    so that each time diferent users access the page , their names get stored in user_name and get displayed on the screen accordingly.
    like if user is anjali, then the name will be stored in variable user_name='anjali'
    and via functioning simlar to print(f"hello {user_name}") -> hello anjali , will be printed.
"""

"""
    in C/C++, variables are made like :
    int name ='anjali'
    where,
    int -> datatype assigned to the variable
    name-> name of variable
    'anjali' -> value assigned to that variable
    -- here, it will give error as name have been already declared as int type variable. string type value can't be assigned to it.
"""

# while in python:
name='anjali' # here, no datatype is assigned to name, this is called dynamic typing
print(name) # output-> anjali

"""
    Dynamic typing : it is the concept according to which, we don't have to assign a datatype to variable as interpreter itself identifies it's type according to value assigned to it.
    and python supports the dynamic typing rather than static typing.
    static typing : typing technique in which the varible is declared with it's predefined datatype , so that value could be assigned to it accordingly.
    example: int a= 5;
    this typing is used in java, c,c++
"""
name='anjali'
print(name) # output-> anjali
print(type(name)) # output-> <class 'str'>
name=55
print(name) # output -> 55
print(type(name)) # output-> <class 'int'>
# here we are able to change datatype of name by changing the value assigned to it, this is the concept of Dynamic binding

"""
    according to dynamic binding a variable is not stuck with one datatype and it's type can be changed like this.
    while in static binding , it is not possible as,
       int a=5;
       a=6; //it's alright but
       a="here"; //is not correct
"""

