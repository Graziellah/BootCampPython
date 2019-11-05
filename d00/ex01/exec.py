import sys

nbArgs = len(sys.argv)
if nbArgs == 1:
    exit()
i = nbArgs - 1
finalString = ""
while i > 0:
    arg = sys.argv[i].swapcase()
    finalString += arg[::-1]
    if i != 1:
        finalString += ' '
    i -= 1
print(finalString)
