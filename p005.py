"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isRemainder(n):
    for i in range(11,21):
        if n % i != 0:
            return False
    return True

num = 2

while True:
    if isRemainder(num):
        break
    else:
        num += 2


print(num)