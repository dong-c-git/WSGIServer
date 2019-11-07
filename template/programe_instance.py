class President:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, President):
            cls.instance = object.__new__(cls)
        return cls.instance


# president1 = President()
# president2 = President()
# print(president1 is president2)

#这段代码运行结果是true, 说明两个变量指向同一块内存，那一块内存地址存放的就是这个类的实例。

# 如果外部修改静态属性instance就可以破坏单例模式的规则。

class President:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, President):
            cls.instance = object.__new__(cls)
        return cls.instance


president1 = President()
President.instance = None
president2 = President()
# print(president1 is president2)
# 修改后两个变量内存地址就不相同了。

# 使用装饰器方式：

def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class President:
    pass


if __name__ == "__main__":
    president1 = President()
    president2 = President()
    # print(president1 is president2)

# 看上去不存在问题了，尝试10个线程时候（不阻塞模式）
from threading import Thread

def singleton(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance

@singleton
class President:
    pass


def target():
    president = President()
    print(president)


# if __name__ == "__main__":
#     threads = [Thread(target=target) for i in range(10)]
#     for thread in threads:
#          thread.start()
#     for thread in threads:
#         thread.join()
# 结果中指向同一内存，因为python有一把GIL大锁，尝试阻塞线程看看。
# 阻塞线程验证结果指向了不同内存，继续优化方案是给装饰器做一个同步；

from threading import Thread, Lock
from time import sleep


def synchronized(func):
    lock = Lock()
    def synchronized_func(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return synchronized_func


def singleton(cls):
    instance = {}
    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class President:
    def __init__(self):
        sleep(1)


def target():
    president = President()
    print(president)

#
if __name__ == '__main__':
    threads = [Thread(target=target) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
