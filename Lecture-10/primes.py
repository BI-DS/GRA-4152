# Caution: This program has bugs.
def main() :
   n = int(input("Please enter the upper limit: "))
   i = 1
   while i <= n :
      if isprime(i) :
         print(i)
      i = i + 2

#  Tests whether an integer is a prime.
#  @param n any positive integer
#  @return True if n is a prime, False otherwise
def isprime(n) :

   if n == 2 :
      # 2 is a prime
      return True
   
   if n % 2 == 0 :   
      # No other even number is a prime
      return False

   # Try finding a number that divides n

   k = 3 # No need to divide by 2 because n is odd
   # Only need to try divisors up to sqrt(n)
   while k * k < n :
      if n % k == 0 :
         # n is not a prime because it is divisible by k
         return False
      # Try next odd number
      k = k + 2

   # No divisor found. Therefore, n is a prime
   return True

# Start the program
main()

