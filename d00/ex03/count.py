import sys
import string

def text_analyzer(text=""):
    if text!="":
        print("The text contains ", str(len(text)) ,  " characters:")
        count = lambda l1,l2: sum([1 for x in l1 if x in l2])
        print("- " ,  sum(1 for c in text if c.isupper()) , " upper letters")
        print("- " , sum(1 for c in text if c.islower()) , " lower letters")
        print("- " , count(text,set(string.punctuation)) , " punctuation marks")
        print("- " , sum(1 for c in text if c.isspace()) , " space" )
    else:
        print("What is the text to analyse?")
