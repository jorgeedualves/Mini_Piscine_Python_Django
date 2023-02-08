import sys
def valid_states(input_user, states, capital_cities):
        if (states[input_user] in capital_cities):
            print(f'{capital_cities[states[input_user]]} is the capital of {input_user}')

def valid_capital(input_user, states, capital_cities):
    for key, value in capital_cities.items():
        if (input_user == value):
            new_value = key
    for key, value in states.items():
        if (new_value == value):
            print(f'{input_user} is the capital of {key}')

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

    text = input_user.split(',')

    for i in text:
        inp = i.strip(' ').title()
        if (inp != ''):
            if (inp in states):
                valid_states(inp, states, capital_cities)
            elif (inp in capital_cities.values()):
                valid_capital(inp, states, capital_cities)
            else:
                print(f'{inp} is neither a city nor a state')

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit()
    countries(sys.argv[1])