import collections

def make_numeric(string):
    cleaned = ''.join([char for char in string if str.isnumeric(char)])
    return cleaned

def make_alpha(string):
    cleaned = ''.join([char for char in string if str.isalpha(char) or char == ' '])
    return cleaned

def sanatize(text):
    # Removes every non-alphanumeric character and makes lowercase
    text = text.lower()
    text = text.replace(',', ' ').replace('.', ' ') # It is important that these become spaces
    text = text.replace('-', ' ').replace('/', ' ') # to segment the words
    text = ''.join([x for x in text if x.isalnum() or x == ' '])
    text = " ".join(text.split()) #Removes whitespace between words
    return(text)

def flatten(l):
# Flattens any nested list - even irregular ones
# See here: https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists/2158532#2158532
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
