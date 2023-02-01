def my_var():
    int0 = 42
    str0 = '42'
    str1 = 'quarante-deux'
    float0 = 42.
    bool0 = True
    list0 = [42]
    dict0 = {42 :42}
    tuple0 = (42,)
    set0 = set()

    print(f'{int0} has a type {type(int0)}')
    print(str0," has a type ",type(str0))
    print(f'{str1} has a type {type(str1)}')
    print(f'{float0} has a type {type(float0)}')
    print(f'{bool0} has a type {type(bool0)}')
    print(f'{list0} has a type {type(list0)}')
    print(f'{dict0} has a type {type(dict0)}')
    print(f'{tuple0} has a type {type(tuple0)}')
    print(f'{set0} has a type {type(set0)}')


if __name__ == '__main__':
    my_var()

