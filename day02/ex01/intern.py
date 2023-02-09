class Intern:
    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'): # Construtor
        self.name = name

    def __str__(self):
        return (f'{self.name}')

    class Coffee:
        def __str__(self):
            return(f'This is the worst coffee you ever tasted')

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')
    
    def make_coffee(self):
        Intern.Coffee()
    
def main():
	no_name = Intern()
	mark = Intern("Mark")
	print(no_name)
	print(mark)
	try:
		no_name.work()
	except Exception as e:
		print(e)
	print(mark.make_coffee())

if __name__ == '__main__':
    main()