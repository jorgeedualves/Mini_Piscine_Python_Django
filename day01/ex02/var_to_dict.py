def dictionary():   
    dic = dict ([
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ])

    dic_new = {}

    for key, value in dic.items():
        if value in dic_new:
            dic_new[value] +=  ' ' + key 
        else:
            dic_new[value] = key
    for key, value in dic_new.items():
        print(key, ':', value)

if __name__ == '__main__':
    dictionary() 