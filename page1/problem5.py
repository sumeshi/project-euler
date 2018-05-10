"""
problem5
---
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import problem3

import math
from functools import reduce

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def m_lcm(*args):
    return reduce(lcm, args)

processing_num = list(filter(lambda i: problem3.is_prime(i), range(1,21)))
print(m_lcm(*processing_num))