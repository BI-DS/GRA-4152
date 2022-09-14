## 
#  This module defines the CashRegister class.
#

## A simulated cash register that tracks the item count and the total amount due.
#
class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   #
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) :
      return self._totalPrice
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) :
      return self._itemCount

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

   ## Adds multiple items, calling self.addItem
   # @param quantity the number of times to add the 
   # given price. @param price as above
   def addItems(self, quantity, price):
      for i in range(quantity):
         self.addItem(price)

   ## Adds multiple items with different prices, 
   # calling self.addItem. 
   # @items_price is a list of tuples 
   # with format (quantity, price)
   def addDiffItems(self, quantity_price):
      for i in range(len(quantity_price)):
         q,p = quantity_price[i]
         self.addItems(q,p)


## 
#  This program tests the two new methods in the 
# CashRegister class.
#

reg = CashRegister()
reg.addItems(4, 3)
print('the no of tot items is {}'.format(reg.getCount()))
print('expected value is 4')
print('the total price is {}'.format(reg.getTotal()))
print('expected value is 12')
reg.addDiffItems([(2,8),(1,10),(3,15)])
print('the no of tot items is {}'.format(reg.getCount()))
print('expected value is 10')
print('the total price is {}'.format(reg.getTotal()))
print('expected value is 83')
        
