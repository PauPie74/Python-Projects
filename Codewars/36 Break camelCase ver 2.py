def solution(s):
    new_s = ""
    for l in s:
        if l == l.upper():
            l = " " + l
        new_s += l
    return new_s