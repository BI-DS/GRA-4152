from fraction import Fraction

a = Fraction(1, 6)
print('Fraction a={}'.format(a))
b = Fraction(1, 3)
c = a + b
print(c)
print("Expected: 1/2")
d = Fraction(4,8)
print(d.numerator)
print('expected numerator: 1')
print(d.denominator)
print('expected denominator: 2')

value1 = Fraction(7, 9)
value2 = Fraction(-5, 12)
value3 = Fraction(4, 8)
result = value1 + value2 - value3
print(result)
print("Expected: -5/36")

if result < value1 or result < value2 :
   print("less than")
else :
   print("not less than")
print("Expected: less than")

print("%.2f" % float(result))
print("Expected: -0.14")

