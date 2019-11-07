#coding:utf-8
from timeit import Timer
from functools import lru_cache
import sys
sys.setrecursionlimit(3000)
import numpy as np
np.set_printoptions(suppress=True)


#使用functools装饰器
@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 2:
        return 1
    else:
        return fib_cache(n-1)+fib_cache(n-2)

if __name__ == "__main__":
    t1 = Timer("fib_cache(20)","from __main__ import fib_cache")
    print("fib_cache(20)",t1.timeit(number=1000),"seconds")

#计算结果
#fib_cache(100) 0.0001750409999999869 seconds
#fib_cache(50) 9.951099999999657e-05 seconds