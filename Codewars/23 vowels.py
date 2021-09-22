# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5

vowels = {'a':'1','e':'2','i':'3','o':'4','u':'5'}

def encode(st):
    en_s = ""
    for letter in st:
        if letter in vowels:
            en_s += vowels[letter]
        else:
            en_s += letter
    return en_s

def decode(st):
    de_s = ""
    for letter in st:
        if letter in "12345":
            for key, value in vowels.items():
                if value == letter:
                    de_s += key
        else:
            de_s += letter
    return de_s

encode('How are you today?')
decode('h2ll4')