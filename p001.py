"""
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

"""

sum3 = 0
sum5 = 0
sum15 = 0

for i in range(334):
    sum3 += 3 * i
    
    if i < 200:
        sum5 += 5 * i

    if i < 67:
        sum15 += 15 * i
    

print(sum3 + sum5 - sum15)