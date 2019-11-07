#coding:utf-8
from timeit import Timer
import sys

def fib(n):
    return fib_be(n,1)

def fib_be(num,sum):
    if num <= 2:
        return 1
    else:
        return fib_be(num-1,num+sum)

if __name__ == "__main__":
    # t1 = Timer("fib_cache(1000)","from __main__ import fib_cache")
    # print("fib_cache(1000)",t1.timeit(number=1000),"seconds")
    t3 = fib(3)
    print(t3)