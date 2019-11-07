from abc import ABC, abstractmethod


class Abstraction(ABC):
    def __init__(self, implementor):
        self.implementor = implementor

    @abstractmethod
    def operation(self):
        pass


class RefinedAbstractionA(Abstraction):
    def operation(self):
        print("RefinedAbstractionA")
        self.implementor.operation_imp()


class RefinedAbstractionB(Abstraction):
    def operation(self):
        print("RefinedAbstractionB")
        self.implementor.operation_imp()


class Implementor(ABC):
    @abstractmethod
    def operation_imp(self):
        pass


class ConcretelmplementorA(Implementor):
    def operation_imp(self):
        print("ConcretlmplementorA")


class ConcretelmplementorB(Implementor):
    def operation_imp(self):
        print("ConcretelmplementorB")


class Client:
    @staticmethod
    def main():
        concrete = input("concrete:")
        abstract = input("abstract:")
        implementor = eval(f"Concretelmplementor{concrete}()")
        implementor.operation_imp()
        abstraction = eval(f"RefinedAbstraction{abstract}(implementor)")


if __name__ == "__main__":
    Client.main()