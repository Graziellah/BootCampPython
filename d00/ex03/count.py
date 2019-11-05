import sys
import string


def count(l1, l2):
    return sum([1 for x in l1 if x in l2])


def text_analyzer(text=""):
    if text != "":
        print("The text contains ", str(len(text)),  " characters:")
        print("- ",  sum(1 for c in text if c.isupper()), " upper letters")
        print("- ", sum(1 for c in text if c.islower()), " lower letters")
        print("- ", count(text, set(string.punctuation)), " punctuation marks")
        print("- ", sum(1 for c in text if c.isspace()), " spaces")
    else:
        print("What is the text to analyse?")
