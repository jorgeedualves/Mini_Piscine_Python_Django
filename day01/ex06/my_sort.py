
def artists():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }

    new_list = list(d.items())

    order = sorted(new_list, key=lambda x:(x[1],x[0]))
    new_disc = dict(order)

    for key, value in new_disc.items():
        print(key, ':', value)

 
            

    # dict_new = {}

    # for key, value in d:
    #     if value in dict_new:
    #         dict_new[value] +=  ' ' + key 
    #     else:
    #         dict_new[value] = key
    # for key, value in dict_new.items():
    #     print(key, ':', value)

if __name__ == '__main__':
    artists()
