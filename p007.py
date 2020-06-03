"""
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
"""
from functions import isPrime

arr = []
i = 1
while len(arr) < 10001:
    if isPrime(i):
        arr.append(i)
    i += 1

print(arr.pop())