##
#  This program computes Fibonacci numbers using a recursive function.
#

def main(n) :
   for i in range(1, n + 1) :
      f = fib(i)
      if i%5 == 0:
        print('processing fib {} out of {}'.format(i,n))
   print("fib(%d) = %d" % (i, f))

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n) :
   if n <= 2 :
      return 1
   else :
      return fib(n - 1) + fib(n - 2)

# python3 -m timeit -s 'from recursivefib import main' -n 1 -r 1 'main(35)'

