"""
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

from functions import isPrime

num = 0
for i in range(2000001):
    if isPrime(i):
        num += i

print(num)