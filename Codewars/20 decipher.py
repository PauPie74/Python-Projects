import re

def decipher_this(string):
    deciphered = ""
    string = string.split()
    for word in string:
        dec_w = ""
        first_l = chr(int(*re.findall(r'\d+',word)))
        word = re.sub(r'\d+','',word)
        l = len(word) - 1
        if l > 0:
            new_word = first_l + word[-1] + word [1:l] + word[0]
        else:
            try:
                new_word = first_l + word[-1] + word [1:l]
            except:
                new_word = first_l
        deciphered += new_word + " "
    deciphered = deciphered[:-1]
    return deciphered