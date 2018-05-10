"""
problem3
---
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

N = 600851475143

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

begin_num = 2
end_num = math.ceil(math.sqrt(N))

processing_data = [i for i in range(begin_num, end_num) if is_prime(i)]

n = max(filter(lambda i: N%i == 0, processing_data))
print(n)