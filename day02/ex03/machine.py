from beverages import HotBeverage, Coffee, Tea ,Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.served = 0

    class EmptyCup(HotBeverage):
        def __init__(self, name='empty cup', price=0.90):
            HotBeverage.__init__(self, name, price)

        def description(self):
            return ("An empty cup?! Gimme my money back!.")

class BrokenMachineException(Exception):
    def __init__(self, error="This coffee machine has to be repaired."):
        Exception.__init__(self, error)
