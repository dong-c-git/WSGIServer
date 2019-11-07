from abc import ABC, abstractmethod


class Receiver:
    pass


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand1(Command):
    def execute(self):
        print('ConcreteCommand1', self.receiver)


class ConcreteCommand2(Command):
    def execute(self):
        print('ConcreteCommand2', self.receiver)


class Invoker:
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()


class Client:
    @staticmethod
    def main():
        receiver = Receiver()
        command = eval(f'ConcreteCommand{input()}(receiver)')
        invoker = Invoker(command)
        invoker.execute()


if __name__ == '__main__':
    Client.main()