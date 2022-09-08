## 
#  This program tests the CashRegister class.
#

from cashregister import CashRegister

register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
print(register1.getCount())
print("Expected: 3")
print("%.2f" % register1.getTotal())
print("Expected: 5.40")
