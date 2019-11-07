#coding:utf-8
from timeit import Timer
import sys
sys.setrecursionlimit(3000)
#使用计算缓存
def cache_fib(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, cache_fib(n-1) + cache_fib(n-2))
    return n
if __name__ == "__main__":
    t1 = Timer("cache_fib(10)","from __main__ import cache_fib")
    print("cache_fib--10", t1.timeit(number=1000), "seconds")

#计算结果：
#cache_fib--10 0.00016871900000003937 seconds