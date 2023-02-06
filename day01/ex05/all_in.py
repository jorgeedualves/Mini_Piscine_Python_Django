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

    if (input_user in capital_cities.values()):
        print(f'{input_user}')
    elif (input_user in states):
        print(f'{input_user}')
        if (states.values() == capital_cities.keys()):
            print(f'{capital_cities.values()}')
    else:
        print(f'{input_user} is neither a capital city nor a state')

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit()
    countries(sys.argv[1])