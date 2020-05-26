import string
from sys import argv

if (len(argv) == 3):
    try:
        numb = int(argv[2])
    except valueError:
        print('ERROR')
        exit()
    if (len(argv[1]) <= numb):
        print('ERROR')
        exit()
    clean_str = argv[1]
    for i in string.punctuation:
        clean_str = clean_str.replace(i, '')
    clean_str = clean_str.split(' ')
    final_list = []
    for x in clean_str:
        if (numb < len(x)):
            final_list.append(x)
    print(final_list)
else:
    print('ERROR')
