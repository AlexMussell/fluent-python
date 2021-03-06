"""
# BEGIN STRATEGY_TESTS
>>> joe = Customer('John Doe', 0)  # <1>
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, .5),
...         LineItem('apple', 10, 1.5),
...         LineItem('watermellon', 5, 5.0)]
>>> Order(joe, cart, fidelity_promo)  # <2>
<Order total: 42.00 due: 42.00>
>>> Order(ann, cart, fidelity_promo)
<Order total: 42.00 due: 39.90>
>>> banana_cart = [LineItem('banana', 30, .5),
...                LineItem('apple', 10, 1.5)]
>>> Order(joe, banana_cart, bulk_item_promo)  # <3>
<Order total: 30.00 due: 28.50>
>>> long_order = [LineItem(str(item_code), 1, 1.0)
...               for item_code in range(10)]
>>> Order(joe, long_order, large_order_promo)
<Order total: 10.00 due: 9.30>
>>> Order(joe, cart, large_order_promo)
<Order total: 42.00 due: 42.00>
"""
# BEGIN STRATEGY

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0



# Note how this is very similar to the classic strat, however we do not specify an abstract base class.
# Instead we create functions which take an order and are passed into the Order class.
# Note how there is no need to instantiate the promo funcs as they are already in use. This reduces cost.
# We can now easily extend this example to have a meta-strat to choost the best promo for a person shop using this functions as object paradigm

promos = [fidelity_promo, large_order_promo, bulk_item_promo]   # List of funcs that are already instantiated

def best_promo(order):
    """Select the best promotional offer"""
    return max(promo(order) for promo in promos)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Command Strat
# The goal of command is to decouple an object thgat invokes and operation, from the provider object that implements it/
# Put the comman object between the 2
# Means the onvoker does not need to know the interface of the reciever. Meaning different recievers can be adapted through command subclass.
# Commands are an OO replacement for callbacks
                                                                                                                                                                                                                     