## Kata not completed ##

import re

def duplicate_encode(word):
    word = word.lower()
    temp = []
    for letter in word:
        if letter in "()":
            temp.append(letter)
        temp2 = []
        for element in temp:
            x = 0
            if x > 1:
                word = word.replace(element, "(")
            else:
                word = word.replace(element, ")")
    for letter in word:
        if letter not in "()":
            searched_letter = re.findall(letter,word)
            if len(searched_letter) == 1:
                word = word.replace(letter, "(")
            else:
                word = word.replace(letter, ")")
    return word

x = "))))((())))()))(()))))()))())(()))))(()"

word = duplicate_encode("@daHvnTydkJSbyyx aPbHPcJk@l!!(GF@!FbeRJ")
if word == x:
    print(True)
else:
    print(False)


x = "))(("
word = duplicate_encode("(( @")
if word == x:
    print(True)
else:
    print(False)
