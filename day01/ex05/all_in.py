import sys
def countries(input_user):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    input_user.split(',')
    print(input_user)
  
    
    for key, value in capital_cities.items():
        if (value.isupper()):
            print ('Está em Maiuscula?', value.isupper())
        if not(input_user in capital_cities.values()):
            print('Unknown capital city')
            sys.exit()

    
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit()
    countries(sys.argv[1])