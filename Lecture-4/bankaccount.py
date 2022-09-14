## A basic bank account that only keeps track of the balance
#  and show how to use class variables and class constants
#
class BankAccount:
    _lastAssignedNumber = 0 # a class variable
    Fee = 30                # a class constant

    ## contructus a bank account with initial balance
    #  incremets the class variable and assign it as
    #  the current account number
    def __init__(self):
        self._balance = 0
        BankAccount._lastAssignedNumber += 1
        self._accountNumber = BankAccount._lastAssignedNumber

    ## Gets the current balance in the account
    #  @return balance
    #
    def getBalance(self):
        return self._balance

    ## Gets the class variable, preserving ecapsulation
    #  @return lastAssignedNumber
    #
    def getLastAssignedNumber(self):
        return BankAccount._lastAssignedNumber

    ## Gets the instance variable account no
    #  @return accountNumber
    #
    def getAccountNumber(self):
        return self._accountNumber

    ## Mutator method that increase the current balance
    #  @param amount A flot number representing deposit 
    #  
    def newDeposit(self, amount):
        self._balance += amount

## Test program
#  add 2 accounts, make some deposits.
#  Then get the LastAssignedNumber and see how it is
#  class specific. On the other hand, AccountNumber
#  is at the object level.
a1 = BankAccount()
a2 = BankAccount()
a1.newDeposit(100)
a2.newDeposit(20)

print('the last assigned no (with a1) is {}'.format(a1.getLastAssignedNumber()))
print('the last assigned no (with a2) is {}'.format(a2.getLastAssignedNumber()))
print('the account no for a1 is {}'.format(a1.getAccountNumber()))
print('the account no for a2 is {}'.format(a2.getAccountNumber()))
print('the account fee is {}'.format(a1.Fee))

