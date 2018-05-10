# coding: utf-8
"""
problem1
---
> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.
"""
import numpy as np

multiple = lambda n: np.arange(n, 1000, n)

duplicate_data = np.r_[multiple(3), multiple(5)]
processing_data = np.unique(duplicate_data)
answer = np.sum(processing_data)

print(answer)