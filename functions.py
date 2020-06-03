import math

def isPrime(n):
    """Returns True if 'n' is a prime number, returns False othervise"""

    if n == 1:
        return False # 1 is not a prime
    
    if n == 2:
        return True

    # if n is even and not 2, its not a prime number
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor ,2):
        if n % i == 0:
            return False
    
    return True