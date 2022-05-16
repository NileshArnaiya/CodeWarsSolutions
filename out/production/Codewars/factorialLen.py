# In this Kata, you will implement a function count that takes an integer and returns the number of digits in factorial(n).

# For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.

# More examples in the test cases.

# Brute force is not possible. A little research will go a long way, as this is a well known series.

# Good luck!
import math
def count(n):
    # ramanujan approach
    #     print(n)
    #     e = 2.71
    #     fact = math.sqrt(3.14)*(n/e)**n
    #     print(fact)
    #     fact *= (((8*n + 4)*n + 1)*n + 1/30.)**(1./6.)
    #     return len(str(round(fact)))
    # alternatively try sterling's approximation of factorial or
    # also could try tree based approaches which are 10x faster than brute force 
    return math.ceil(math.lgamma(n+1)/math.log(10))