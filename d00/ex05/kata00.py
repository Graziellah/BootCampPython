t = (19,42,21)


lenght = len(t)
finalSentence = "The " + str(lenght) + " numbers are: "
for i in range(0, lenght):
    finalSentence += str(t[i])
    if i != lenght - 1:
        finalSentence += ", "

print(finalSentence)
