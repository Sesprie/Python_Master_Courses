# -*- coding: utf-8 -*-
# @Time    : 2019-04-21 11:39
# @Author  : play4fun
# @File    : primes.py
# @Software: PyCharm

"""
primes.py:
"""
import traceback
from datetime import datetime


def primes(kmax):
    """标准Python语法下的素数计算"""

    p = range(1000)
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result
