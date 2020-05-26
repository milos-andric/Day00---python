from sys import argv

if len(argv) > 2:
    print("ERROR")
elif len(argv) == 2:
    try:
        number = int(argv[1])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")
