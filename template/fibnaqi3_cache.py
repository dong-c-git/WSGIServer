#coding:utf-8
from timeit import Timer
import cache
import sys
sys.setrecursionlimit(3000)

@cache.cache(timeout=20,fname="my_cache.pkl")
def fib_cache(n):
    if n <= 2:
        return 1
    else:
        return fib_cache(n-1)+fib_cache(n-2)

if __name__ == "__main__":
    t1 = Timer("fib_cache(100)","from __main__ import fib_cache")
    print("fib_cache(100)",t1.timeit(number=1000),"seconds")

#计算结果：
#fib_cache(100) 0.39800654799999996 seconds
#fib_cache(100) 0.39572887799999995 seconds