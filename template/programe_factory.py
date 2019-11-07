#coding:utf-8
from abc import ABC, abstractmethod


class Client:
    @staticmethod
    def main():
        option = input("A:ProductA,B:productB\n请选择：").strip().upper()
        creator = None
        # 创建工厂子类对象creator
        if option == 'A':
            creator = CreatorA()
        elif option == 'B':
            creator = CreatorB()
            # 调用工厂方法，获得一个具体的产品子类对象
        product = creator.factory()
        # 使用该产品子类对象做相应的操作
        print(product.get_info())


# 工厂类的接口及其实现子类，每个工厂子类仅仅负责创建一种产品对象。每个工厂子类都不包含条件语句。
class Creator(ABC):
    @abstractmethod
    def factory(self):
        pass


class CreatorA(Creator):
    def factory(self):
        return ProductA()


class CreatorB(Creator):
    def factory(self):
        return ProductB()


# 以下类为产品接口及其实现子类
class Product(ABC):
    @abstractmethod
    def get_info(self):
        pass


class ProductA(Product):
    def get_info(self):
        return "ProductA"


class ProductB(Product):
    def get_info(self):
        return "ProductB"


if __name__ == '__main__':
    Client.main()