class HotBeverage:
    def __init__(self,name = 'hot beverage',price = 0.30):

        self.name = name
        self.price = price

    def description(self):
        return (f'Just some hot water in a cup.')
    
    def __str__(self):
        return (f'name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}')
    
class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(name="coffee", price=0.40)
    
    def description(self):
        return (f'A coffee, to stay awake.')      

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name="tea")

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(name="chocolate", price=0.50)

    def description(self):
        return (f'Chocolate, sweet chocolate...')
     
class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)
    
    def description(self):
        return (f'Un po di Italia nella sua tazza!')

def main():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())
    
if __name__ == '__main__':
    main()
    