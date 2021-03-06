"""
problem3
---
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

if __name__ == '__main__':
    N = 600851475143

    begin_num = 2
    end_num = math.ceil(math.sqrt(N))

    processing_data = [i for i in range(begin_num, end_num) if (i%2!=0) and (i%3!=0) and (i%5!=0) and is_prime(i)]

    n = max(filter(lambda i: N%i == 0, processing_data))
    print(n)