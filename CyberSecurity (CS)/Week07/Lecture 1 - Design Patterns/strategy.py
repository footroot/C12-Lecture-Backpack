class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Strategy B")

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

context = Context(ConcreteStrategyA())
context.execute_strategy()

context = Context(ConcreteStrategyB())
context.execute_strategy()