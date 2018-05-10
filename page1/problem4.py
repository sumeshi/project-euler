"""
problem4
---
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def palindrome():
    m = []
    for i in range(100, 1000)[::-1]:
        for j in range(100, i)[::-1]:
            num = i*j
            if str(num)[::-1] == str(num):
                m.append(num)
    return max(m)

print(palindrome())