import string
from sys import argv

str = " ".join(argv[1:])
str = str[::-1]
str = str.swapcase()
print(str)
