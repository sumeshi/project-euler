"""
problem4
---
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def palindrome():
    l = m = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i*j
            if str(num)[::-1] == str(num):
                l.append(num)
        if len(l)>0: m.append(max(l))
    return max(m)
                
print(palindrome())