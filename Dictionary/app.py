import json
from difflib import get_close_matches as gcm
"""get json data in python dict and save in a variable"""
data = json.load(open("data.json"))

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(gcm(word, data.keys())) > 0:
        yorn = input('Did you mean %s instead? Enter y if yes and n if no: ' % gcm(word, data.keys())[0])
        yorn = yorn.lower()
        if yorn == 'y':
            return data[gcm(word, data.keys())[0]]
        elif yorn == 'n':
            return 'We could not find this word'
        else:
            return 'We could not understand your entry'
    else:
        return 'We could not find this word'

word = input("Enter a word: ")

output = (get_definition(word))
if type(output) == list:
    number = 1
    for item in output:
        print(str(number) + ') ' + item)
        number += 1
else:
    print(output)