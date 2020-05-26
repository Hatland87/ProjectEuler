"""
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
6857
"""
import math

num = 600851475143

def isPrime(n):
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    
    return True

x = 2
ans = 0

while num > 1:
    if(num % x == 0):
        if(isPrime(x)):
            num = num / x
            ans = x
    x += 1

print(ans)