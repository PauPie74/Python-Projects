def pig_it(text):
    a = '''!@#$%^&*(){}[]?/'"'''
    x = text.split()
    words = []
    for w in x:
        if w not in a:
            words.append(w[1:]+w[0]+'ay')
        else:
            words.append(w)
    piglatin = ""
    for ele in words:
        piglatin = piglatin + " " + ele
    piglatin = piglatin.strip()
    return piglatin
