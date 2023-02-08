import sys

def curriculum(file):

    content = open('myCV.template', 'r').read()
    content_set = open('settings.py', 'r').read()

    new_dict = {}

    for i in filter(None, content_set.split('\n')):
        print (i)
        new_dict[i.split('=')[0].strip(" '")] = i.split('=')[1].strip(" '")
    print(new_dict)

    text = content.format(**new_dict)
    print(text)


    new_file = open('myCV.html', 'w')
    new_file = text

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit()
    curriculum(sys.argv[1])

