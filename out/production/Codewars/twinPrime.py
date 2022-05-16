# A twin prime is a prime number that differs from another prime number by 2. Write a function named is_twin_prime which takes an int parameter and returns true if it is a twin prime, else false.

# example:

# given 5, which is prime
# 5+2=7 which is prime 
# 5-2=3 which is prime
# Hence , 5 has two prime twins and its a Twin Prime.
# ---------------------------------------------------
# given 7, which is prime
# 7-2=5 which is prime
# 7+2=9 which is not prime
# Hence, 7 has one prime twin, and its a Twin Prime.
def is_twinprime(n):
    
    if n > 1:
        count = 0
        flag = False
        for i in range(2,n):
            if (n % i) == 0:
                 flag = True
                 break
        if flag:
            return False
        else:
            flagger = False
            flagger2 = False 
            for k in range(2, n+2):
                if ((n+2) % k) == 0:
                    flagger = True
                    break
            if not flagger:
                count+=1 
                return True
        n = n - 2
        for j in range(2, n):
            if (n % j) == 0:
                flagger2 = True
                break
        if not flagger2:
            count+=1
            return True
        else:
            return False
                
        if count >=1:
            return True
        else:
            return False
    else:
        return False
