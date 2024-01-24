import re

def xo(s):
    s = s.lower()
    number_of_x = len(re.findall("x",s))
    number_of_o = len(re.findall("o",s))
    if number_of_x == number_of_o:
        return True
    else:
        return False
