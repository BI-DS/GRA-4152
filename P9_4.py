## A class that contains the data of the assigned address.
# Class parameters are: House number, City, State, Postal code, Apartment name--not mandatory
class Address():
    def __init__(self, house_num, street, city, state, postal_code, apt_name=""):
        self._house_num = house_num
        self._street = street
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._apt_name = apt_name
    
    ## Prints the instance variables with the exception of apartment number
    def print(self):
        print(f"{self._street}, {self._house_num}\n{self._city}, {self._state}, {self._postal_code}")

    ## Checks whether the argument is before or after the instance variable postal code value.
    # Returns True if the instance variable is less than the argument value returns False otherwise
    def comesBefore(self, other):
        return self._postal_code < other