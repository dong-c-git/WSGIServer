#coding:utf-8
from time import ctime, sleep
#装饰函数有参数
def timefun(func):
    def wrapped_func(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrapped_func

@timefun
def foo(a, b):
    print(a+b)

foo(3,5)
sleep(2)
foo(2,4)

from time import ctime, sleep
#装饰函数有不定长参数
def timefun(func):
    def wrapped_func(*args, **kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        print(args,kwargs)
        func(*args, **kwargs)
    return wrapped_func

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3,5,7)
sleep(2)
foo(2,4,9)
from time import ctime, sleep
#装饰器中有return
def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        return func()
    return wrapped_func

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

foo()
sleep(2)
getInfo()

print(getInfo())

#decorator2.py

from time import ctime, sleep
#装饰器带参数
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrapped_func():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        return wrapped_func
    return timefun

# 下面的装饰过程
# 1. 调用timefun_arg("itcast")
# 2. 将步骤1得到的返回值，即time_fun返回， 然后time_fun(foo)
# 3. 将time_fun(foo)的结果返回，即wrapped_func
# 4. 让foo = wrapped_fun，即foo现在指向wrapped_func
@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")
foo()
sleep(2)
foo()
too()
sleep(2)
too()

#类装饰器
class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()

@Test
def test():
    print("----test---")
test()
