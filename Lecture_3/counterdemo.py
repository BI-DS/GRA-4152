##
#  This program demonstrates the Counter class.
#

# Import the Counter class from the counter module. 
from counter import Counter

tally = Counter()
tally.reset()
tally.click()
tally.click()

result = tally.getValue()
print("Value:", result)

tally.click()
result = tally.getValue()
print("Value:", result)

