

## Here we should add the checkout essentials, and the func tions beneath each one of them. 

# 1. Cart: > add to cart, remove from cart, clear the cart. 
# 2. Checkout: > calculate the items count, calculate the total price, choosing the payment method.


from flask import session,Flask

app = Flask(__name__)

class Cart: 
    def __init__(self) -> None:
        pass

    @app.route('/add_to_cart/<int:item_id>')    
    def add_to_cart(self,item_id): 
        cart_items = session.get('cart',[])
        return cart_items
    
    def remove_from_cart(self,item_id): 
        cart_items = session.get('cart',[])
        remove = [ i.pop() for i in cart_items if i == item_id]
        return remove
    
    def clear_cart(self):
        # cart_items = session.get('cart',[])
        pass

class Checkout: 
    def __init__(self) -> None:
        pass

