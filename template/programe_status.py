from abc import ABC,abstractmethod
class State(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteStateA(State):
    def operation(self):
        print("ConcretaStateA")

class ConcreteStateB(State):
    def operation(self):
        print("ConcretaStateB")

class Context:
    def __init__(self,state):
        self.state = state

    def request(self):
        self.state.operation()

class Client:
    @staticmethod
    def main():
        state = ConcreteStateA()
        context = Context(state)
        context.request()
        state = ConcreteStateB()
        context.state = state
        context.request()

if __name__ == "__main__":
    Client.main()
