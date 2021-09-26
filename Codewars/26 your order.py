def order(sentence):
    s = sentence.split()
    n_str = ""
    o = 1
    if sentence != "":
        while len(n_str) != (len(sentence)+1):
            for w in s:
                for l in w:
                    if l.isdigit():
                        if int(l) == o:
                            n_str = n_str + w + " "
                            o += 1
        n_str = n_str.rstrip()
    print(n_str)
    return n_str