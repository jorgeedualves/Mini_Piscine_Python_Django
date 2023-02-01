def read_numbers():
    numbers = open("numbers.txt", "r")
    for line in numbers:
        contents = line.split(',')
    for temp in contents:
        print(temp.strip('\n'))
    numbers.close()

if __name__ == '__main__':
    read_numbers()