import re
def count_deaf_rats(town):
    p_loc = town.index('P')
    l_town = len(town)
    left = town[0:p_loc]
    right = town[p_loc+1:l_town]
    l_rats = re.findall(r'O~|~O', left)
    r_rats = re.findall(r'O~|~O', right)
    d_rat = 0
    if p_loc == 0:
        #p is left
        for rat in r_rats:
            if rat == "~O":
                d_rat += 1
    elif p_loc == len(left) and p_loc < len(left)+len(right):
        #pp is in the center
        for rat in l_rats:
            if rat == "O~":
                d_rat += 1
        for rat in r_rats:
            if rat == "~O":
                d_rat += 1
    elif p_loc == len(left):
        # pp is right
        for rat in l_rats:
            if rat == "O~":
                d_rat += 1
    return d_rat



#P = The Pied Piper
#O~ = Rat going left
#~O = Rat going right


count_deaf_rats("~O~O~O~O P") #0 right
count_deaf_rats("P O~ O~ ~O O~") #1 right
count_deaf_rats("~O~O~O~OP~O~OO~") #2