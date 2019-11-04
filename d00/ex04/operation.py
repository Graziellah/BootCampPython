import sys


def operations(nb1, nb2):
    print("Sum:", nb1 + nb2)
    print("Difference:", nb1 - nb2)
    print("Product:", nb1 * nb2)
    try:
        print("Quotient:", nb1/nb2)
    except ZeroDivisionError:
        print("Quotient :ERROR (div by zero)")
    try:
        print("Reminder:", nb1%nb2)
    except ZeroDivisionError:
        print("Reminder: ERROR (modulo by zero)")

try:
    nbArgs = len(sys.argv)
    if nbArgs == 3:
        if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
            operations(int(sys.argv[1]), int(sys.argv[2]))
        else:
            raise TypeError("only numbers")
    else:
        raise ValueError(" too many arguments")
except (TypeError, ValueError) as err :
    print("InputError:" ,err)
    print("Usage: python operations.py")
    print("Exemple: \n \tpython operations 10 3")
