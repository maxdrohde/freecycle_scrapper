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
