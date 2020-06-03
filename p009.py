"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2
    
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

# a^2 + b^2 = c^2   ->  sqrt(a^2 + b^2) = c
# a + b + c = 1000  ->  a + b + sqrt(a^2 + b^2) = 1000
# a < b < sqrt(a^2 + b^2)

import math

for b in range(1, 1001):
    for a in range(1, b):
        c = math.sqrt(math.pow(a,2) + math.pow(b,2))
        if a + b + c == 1000:
            print(math.floor(a*b*c))