#coding:utf-8
from timeit import Timer
from diskcache import FanoutCache
import sys
sys.setrecursionlimit(3000)

#缓存临时文件位置
cache = FanoutCache('tmp/diskcache/fanoutcache')

@cache.memoize(typed=True,expire=None,tag='fib_disk')
def fib_disk(n):
    if n <= 2:
        return 1
    else:
        return fib_disk(n-1)+fib_disk(n-2)

if __name__ == "__main__":
    t1 = Timer("fib_disk(100)","from __main__ import fib_disk")
    print("fib_disk(100)",t1.timeit(number=1000),"seconds")

#计算结果：
#fib_disk(100) 0.12914266199999996 seconds
#fib_disk(100) 0.129672597 seconds