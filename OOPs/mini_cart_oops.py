# Mini-Project: Simple Shopping Cart

# Create a simple shopping cart system with the following features:

# Add items to the cart.
# Remove items from the cart.
# View the items in the cart.
# Calculate the total cost of the items in the cart.


class ShoppingCart:

    cart={'product':[],'price':[],'number':[]}

    def __init__(self,prod_name,prod_price, quantity):
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.quantity = quantity

        self.add_items()

    def add_items(self):
        # to check if item is added in cart or not
        # using enumerate, it iterate over list, tuple etc and returns index and item in that datatype
        for i, item in enumerate(ShoppingCart.cart['product']):
            if item == self.prod_name:
                ShoppingCart.cart['number'][i] += self.quantity
                break
        else:
            # to add a new item in cart
            ShoppingCart.cart['product'].append(self.prod_name)
            ShoppingCart.cart['price'].append(self.prod_price)
            ShoppingCart.cart['number'].append(self.quantity)

    @staticmethod
    def remove_items(product,number):
        for i, item in enumerate(ShoppingCart.cart['product']):
            if item == product:
                ShoppingCart.cart['number'][i] -= number
                if ShoppingCart.cart['number'][i] <1:
                    del ShoppingCart.cart['product'][i]
                    del ShoppingCart.cart['price'][i]

    @staticmethod
    def view_cart():
        print(ShoppingCart.cart)


    def decorator(func):
        def wrapper(*args):
            if all(isinstance(i,int) for i in ShoppingCart.cart['price']):
                print("your total cost is :")
                result= func(*args)
                return result
            else:
                print("there seems to be a issue ")
        return wrapper

    @staticmethod
    @decorator
    def total_amount():
        total =0
        for i, items in enumerate(ShoppingCart.cart['price']):
            total += ShoppingCart.cart['price'][i] * ShoppingCart.cart['number'][i]
        return total




s= ShoppingCart('laptop',2000,1)
s1=ShoppingCart('mobile',300,1)
s2=ShoppingCart('cup',50,3)
s4= ShoppingCart('laptop',2000,1)
ShoppingCart.remove_items('cup',2)
ShoppingCart.view_cart()
ShoppingCart.total_amount()



"""output example:
            {'product': ['laptop', 'mobile', 'cup'], 'price': [2000, 300, 50], 'number': [2, 1, 1]}
            your total cost is :
            4350
"""