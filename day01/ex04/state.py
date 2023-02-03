import sys
def countries(argv):
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

    if not(argv[1] in capital_cities.values()):
        print('Unknown capital city')
        sys.exit()
    for key, value in capital_cities.items():
        if (argv[1] == value):
            new_value = key
    for key, value in states.items():
        if (new_value == value):
            print(key)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit()
    countries(sys.argv)