import sys

try:
    if len(sys.argv) == 2 and sys.argv[1].isnumeric():
        nb = int(sys.argv[1])
        if nb == 0:
            print("I'm Zero.")
        elif nb % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    elif len(sys.argv) == 1:
        exit()
    else:
        raise (ValueError)
except ValueError:
    print("ERROR")
