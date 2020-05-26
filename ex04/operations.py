import math
from sys import argv

msg_error1 = ""
msg_error2 = ""
errored = 0
if (len(argv) > 3):
    msg_error1 = "InputError: too many arguments\n\n"
    errored = 1
if (len(argv) < 3):
    errored = 1
if ((len(argv) == 3) and (errored == 0)):
    try:
        nb1 = int(argv[1])
        nb2 = int(argv[2])
        add = nb1 + nb2
        diff = nb1 - nb2
        product = nb1 * nb2
        if nb2 == 0:
            div = "ERROR (div by zero)"
            mod = "ERROR (modulo by zero)"
        else:
            div = nb1 / nb2
            mod = nb1 % nb2
        print("Sum:\t\t" + str(add))
        print("Difference:\t" + str(diff))
        print("Product:\t" + str(product))
        print("Quotient:\t" + str(div))
        print("Remainder:\t" + str(mod))
    except ValueError:
        errored = 1
        msg_error1 = "InputError: only numbers\n\n"

if errored:
    if len(msg_error1) != 0:
        print(msg_error1)
    print("Usage: python operations.py <number1> <number2>\nExample:")
    print("\tpython operations.py 10 3")
