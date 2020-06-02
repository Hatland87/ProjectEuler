"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
ans = 0

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        n = i*j
        if (str(n) == ''.join(reversed(str(n)))):
            if (n > ans):
                ans = n

print(ans)
