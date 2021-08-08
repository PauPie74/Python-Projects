def solution(s):
    sentence = ""
    for letter in s:
        if letter.isupper():
            sentence += " "+letter
        else:
            sentence += letter
    return sentence