class House:
    def __init__(self, price=0):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price

    @price.deleter
    def price(self):
        del self._price
        self._price = 0


## Test file
#
house = House(6)
# XXX using decorator as getter
print('The house price is {} millions Kr.'.format(house.price))
# XXX using decorator as setter 
house.price = 6.5
print('Sorry, that price is wrong. The correct price is {} millions'.format(house.price))
# XXX using decorator as deleter
del house.price
print('I am not sure any more about the price, I\'ll ask. Price = {}'.format(house.price))
