#coding:utf-8
from abc import ABC,abstractmethod

class Strategy(ABC):
    @abstractmethod
    def algorithm_interface(self,context):
        pass

class ConcreteStrategyA():
    def algorithm_interface(self,context):
        print("ConcreteStrategyA")

class ConcreteStrategyB(Strategy):
    def algorithm_interface(self,context):
        print('ConcreteStrategyB')

class ConcreteStrategyC(Strategy):
    def algorithm_interface(self,context):
        print('ConcreteStrategyc')

class Context:
    def __init__(self,strategy):
        self.strategy = strategy

    def context_interface(self):
        self.strategy.algorithm_interface(self)

class Client:
    @staticmethod
    def main():
        strategy = eval(f'ConcreteStrategy{input()}()')
        context = Context(strategy)
        context.context_interface()

if __name__ == '__main__':
    Client.main()