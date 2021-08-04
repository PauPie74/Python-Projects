def find_next_square(sq):
    r = sq**(0.5)
    if r-int(r) == 0:
        square = int((r+1)*(r+1))
        return square
    else:
        return -1