def alphabet_position(text):
    t = text.lower()
    s = ""
    for letter in t:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            x = ord(letter)-96
            n = str(x)
            s += n + ' '
    s = s.rstrip()
    return s