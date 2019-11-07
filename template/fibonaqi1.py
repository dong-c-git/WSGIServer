#coding:utf-8
from timeit import Timer
import sys
sys.setrecursionlimit(3000)

#没有使用缓存的斐波那契数列
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    t1 = Timer("fib(20)","from __main__ import fib")
    # 斐波那契数列递归深度1000，计算1000次时间
    print("fib--20", t1.timeit(number=1000), "seconds")
#计算结果
#fib--50 1.708622157 seconds
#fib--50 1.689655434 seconds