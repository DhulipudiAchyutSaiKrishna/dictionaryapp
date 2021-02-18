import json

data = json.load(open('data.json'))

def meaning(word):
    return data[word]

 word = input("Enter the word to get the meaning : ")

 print(meaning(word))