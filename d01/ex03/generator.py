import random


def wordisplay(arrayText):
    for word in  arrayText:
        yield word

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    optionsChoice = ['shuffle', 'ordered', 'unique']
    if option == None or option in optionsChoice or not isinstance(text, str):
        rawText = text.split(sep)
        displayText =  ""
        if option == 'ordered':
            displayText = sorted(rawText, key=str.lower)
        elif option  ==  'shuffle':
            random.shuffle(rawText)
            displayText  = rawText
        elif option == 'unique':
            displayText = []
            for word in rawText:
                if word not in displayText:
                    displayText.append(word)
        else:
            displayText = rawText
        wordgene = wordisplay(displayText)
        print('...     print(word)')
        print('...')
        for i in wordgene:
            print(i)
    else:
        print('ERROR')