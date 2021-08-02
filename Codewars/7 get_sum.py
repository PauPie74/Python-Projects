def get_sum(a,b):
    if a == b:
        return a
    else:
        if a > b:
            bigger = a
            smaller = b
        else:
            bigger = b
            smaller = a
        s = 0
        while smaller <= bigger:
            s += smaller
            smaller += 1
    return s