"""
problem5
---
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import problem3

def min_multiple():
    processing_num = range(1,21)[::-1]
    n = 20

    while(True):
        for i in processing_num:
            if n%i != 0: break
            if i == 1: return n*i
        n+=1

print(min_multiple())
