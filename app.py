import json

data = json.load(open('data.json'))

def meaning(word):
    return data[word]

 