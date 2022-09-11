## Creates a customer class that stores the total amount of purchases and sees whether they've reached the amount for the assigned promotion.
class Customer():
    def __init__(self):
        self._total_purchases = 0

    ## Stores the amount purchased by the consumer, if the customer has reached the discount amount, the discount will be applied and
    ## instance variable, total purchases will be set to 0 again, for the possibilites of the next discount
    # 1 required argument, which is the amount of the good that's bought in USD.
    def makePurhcase(self, amount):
        if self.discountReached() is True:
            self._total_purchases = 0
            self._total_purchases += (amount * .1) - amount
        else:
            self._total_purchases += amount

    ## Checks whether the customer have accumulatively reached the discount price which is 100$.
    # Returns True if the customer have qualified for the discount and returns False if not.
    def discountReached(self):
        return self._total_purchases >= 100
    
## The assigned test functions to see if the code works properly.
# Firs test function tests if the discountReached method recognizes the discount
def test_loyal_cus_prom():
    loyal_cus = Customer()
    loyal_cus.makePurhcase(10000)
    loyal_cus.discountReached()
    assert loyal_cus.discountReached() == True

# Second function checks if the discount is applied, and checks if the customer is not qualified for another discount.
def test_loyal_cus_second_purchase():
    loyal_cus = Customer()
    loyal_cus.makePurhcase(10000)
    loyal_cus.makePurhcase(100)
    assert loyal_cus.discountReached() == False