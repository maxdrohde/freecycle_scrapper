def make_numeric(string):
    cleaned = ''.join([char for char in string if str.isnumeric(char)])
    return cleaned

def make_alpha(string):
    cleaned = ''.join([char for char in string if str.isalpha(char) or char == ' '])
    return cleaned
