##
#  Compute the total cost of owning a car for 5 years, ignoring financing.
#

# Define constants.
NUM_YEARS = 5

# Read input from the user.
car_cost = float(input("Enter the cost of the car: "))
km_per_year = float(input("How many km will you drive each year? "))
gas_price = float(input("Enter the price of gas per liter: "))
efficiency = float(input("Enter the fuel efficiency in km/L: "))
resale = float(input("How much can you sell the car for after 5 years? "))

# Compute the total cost of ownership.
total_cost = car_cost - resale + \
             NUM_YEARS * km_per_year / efficiency * gas_price

# Display the result.
print("The total cost of ownership is %.2f." % total_cost)

