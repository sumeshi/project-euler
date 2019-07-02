"""
problem7
---
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from math import sqrt, ceil

def is_prime(n):
    proc_list = [i for i in range(3, ceil(sqrt(n))+1, 2)]
    for i in proc_list:
        if n % i == 0: return False
    return True

def gen_prime(num):
    while True:
        if is_prime(num): yield num
        num += 2

def num_of_prime(n):
    p = gen_prime(3)
    for _ in range(n-2):
        next(p)
    else:
        prime = next(p)
    return prime
 
print(num_of_prime(10001))