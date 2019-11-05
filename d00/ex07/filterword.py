import sys


def filtwords(string, maxLength):
    finalElem = []
    splittedString = string.split()
    stringLen = len(splittedString)
    for i in range(0, stringLen):
        if len(splittedString[i]) > maxLength:
            finalElem.append(splittedString[i])
    return finalElem


if len(sys.argv) == 3 and not sys.argv[1].isnumeric():
    rest = filtwords(sys.argv[1],  int(sys.argv[2]))
    print(rest)
else:
    print("ERROR")
