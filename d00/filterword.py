import sys


def filtWord(string, maxLength):
    finalElem = []
    for idx, val in enumerate(string):
        if len(val) > maxLength:
            finalElem.append(val)
    return finalElem

if len(sys.argv) == 3:
    rest = filtWord(sys.argv[1]. sys.argv[2])
    print (rest)
else:
    print("ERROR")
