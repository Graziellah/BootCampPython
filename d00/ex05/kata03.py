phrase = "The right format"

lengthPhrase = len(phrase)

displayingLine = ""

for i in range(1, 42 - lengthPhrase):
    displayingLine += "-"

displayingLine += phrase

print(displayingLine)
