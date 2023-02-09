class Intern:
    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'): # Construtor
        self.name = name

    def __str__(self):      # metodo
        return f'{self.name}'

    class Coffee:
        def __str__(self):
            return(f'This is the worst coffee you ever tasted')

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')
    
    def make_coffee(self):
        Intern.Coffee()

if __name__ == '__main__':
    
    try:
        Intern.make_coffee()
    except Exception as erro:
       Intern.work()
    else:
        print('fim')
