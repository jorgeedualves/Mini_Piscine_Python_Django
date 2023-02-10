import sys
import os

def curriculum(file):

    content = open(file, 'r').read()
    content_set = open('settings.py', 'r').read()

    new_dict = {}

    for i in filter(None, content_set.split('\n')):
        # print (i)
        new_dict[i.split('=')[0].strip(" '")] = i.split('=')[1].strip(" '")
    # print(new_dict)

    text = content.format(**new_dict)
    # print(text)

    file_name = file.replace('.template', '.html')
    print(file_name)
    
    output_file = open(file_name, 'w')
    output_file.write(text) 

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit('Number of invalid arguments')
    if not (sys.argv[1].endswith('.template')):
        sys.exit('Invalid extension')
    if not (os.path.isfile(sys.argv[1])):
        sys.exit("File doesn't exist")
    curriculum(sys.argv[1])

