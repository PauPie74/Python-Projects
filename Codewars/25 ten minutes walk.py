def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0
    if len(walk) == 10:
        for d in walk:
            if d == 'n':
                n += 1
            elif d == 's':
                s += 1
            elif d == 'e':
                e += 1
            elif d == 'w':
                w += 1
        if n == s and e == w:
            return True
        else:
            return False
    else:
        return False