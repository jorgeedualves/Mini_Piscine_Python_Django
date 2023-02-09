from beverages import HotBeverage, Coffee, Tea ,Chocolate, Cappuccino
import random

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

    def repair(self):
        self.served = 0
        print("----------\nMachine Repaired\n------------")
    
    def serve(self, product):
        list_product = [product(), CoffeeMachine.EmptyCup()]
        print(random.choice(list_product))

def main():
    
	dict_products = {0 : HotBeverage, 1 : Coffee, 2 : Tea, 3 : Chocolate, 4 : Cappuccino}
	for i in range(2):
		try:
			machine = CoffeeMachine()
			for i in range(10):
				machine.serve(dict_products.get(random.randint(0, 4)))
			raise machine.BrokenMachineException()
		except Exception as e:
			print(e)
			machine.repair()

if __name__ == '__main__':
    main()


