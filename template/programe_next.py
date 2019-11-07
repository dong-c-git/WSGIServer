from abc import ABC,abstractmethod


class Aggregate(ABC):

    @abstractmethod
    def create_iterator(self):
        pass


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.data_structure = list(range(10))

    def create_iterator(self):
        return Concretelterator(self)


class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current_item(self):
        pass


class Concretelterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.first()

    def first(self):
        self.index = 0

    def next(self):
        self.index += 1

    def is_done(self):
        if self.index == len(self.aggregate.data_structure):
            return True
        return False

    def current_item(self):
        return self.aggregate.data_structure[self.index]


class Client:
    @staticmethod
    def main():
        aggregate = ConcreteAggregate()
        iterator = aggregate.create_iterator()
        while not iterator.is_done():
            print(iterator.current_item())
            iterator.next()


if __name__ == "__main__":
    Client.main()