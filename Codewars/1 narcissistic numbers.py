def narcissistic(value):
    vs = str(value)
    l = int(len(vs))
    sum = 0
    for digit in vs:
        d = int(digit)
        res = d ** l
        sum += res
    if sum == value:
        return True
    else:
        return False