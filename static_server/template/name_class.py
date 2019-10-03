class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        if self.original_price:
            new_price = self.original_price * self.discount
        else:
            new_price = self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

obj = Goods()
print(obj.price)         # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价
print(obj.discount)

#coding=utf-8
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar,set_bar,del_bar,"this is description")

obj = Foo()
obj.BAR
obj.BAR = "test set"
desc = Foo.BAR.__doc__
print(desc)
del obj.BAR


class Foo:
    def __init__(self):
        print("this is init")

    def __call__(self):
        print("__call__")


obj = Foo()  # 执行__init__
#obj()  # 执行__call__

class Province(object):
    country = "China"

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print("func")


# 获取类的属性，即：类属性、方法
print(Province.__dict__)
