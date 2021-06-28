from decimal import Decimal

from django.shortcuts import get_object_or_404

from feastfreedom.settings import SESSION_ID_CART
from kitchen.models import Food


class Cart(object):
    def __init__(self, request):
        # 1. Get hold of session of request and response object
        # 2. Assign Web Application level session Id to this object
        # 3. If the object is not created yet, then create a object
        self.session = request.session
        if not self.session.get(SESSION_ID_CART):
            self.session[SESSION_ID_CART] = {}
        self.session_cart_obj = self.session[SESSION_ID_CART]

    def addnew(self, product):
        product_id = str(product.id)
        if product_id not in self.session_cart_obj:
            self.session_cart_obj[str(product_id)] = dict(quantity=0, price=str(product.price))
        self.session_cart_obj[str(product_id)]['quantity'] += 1
        self.session[SESSION_ID_CART] = self.session_cart_obj
        self.session.modified = True

    def removeone(self, product_id):
        if str(product_id) in self.session_cart_obj:
            if self.session_cart_obj[str(product_id)]['quantity'] <= 0:
                del self.session_cart_obj[str(product_id)]
            else:
                self.session_cart_obj[str(product_id)]['quantity'] -= 1
        self.session[SESSION_ID_CART] = self.session_cart_obj
        self.session.modified = True

    def __iter__(self):
        product_ids = self.session_cart_obj.keys()
        # get the product objects and add them to the cart
        products = Food.objects.filter(id__in=product_ids)
        for product in products:
            self.session_cart_obj[str(product.id)]['product'] = product
        for item in self.session_cart_obj.values():
            item['price'] = item['price']
            item['total_price'] = Decimal(item['price']) * Decimal(item['quantity'])
            yield item

    def clearSession(self):
        self.session_cart_obj = self.session[SESSION_ID_CART] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.session_cart_obj.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.session_cart_obj.values())

    def clear(self):
        print('in cart clear')
        self.session_cart_obj = {}
        self.session[SESSION_ID_CART] = {}

    def getKey(self, item):
        return list(self.session_cart_obj.keys())[list(self.session_cart_obj.values()).index(item)]

    def __str__(self):
        return str(self.session_cart_obj)