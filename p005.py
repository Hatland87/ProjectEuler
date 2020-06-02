"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Must be even number
# 20 10 
# 19
# 18 9 3
# 17
# 16 4
# 15
# 14 7
# 13
# 12 6
# 11
# 5

# 10
# 9 3
# 8 
# 7

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