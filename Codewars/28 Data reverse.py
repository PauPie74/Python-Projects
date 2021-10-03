def data_reverse(data):
    data_list = []
    string = ''
    y = 0
    for x in data:
        if y <= 8:
            y+= 1
            string += str(x)
            if y == 8:
                y = 0
                data_list.append(string)
                string = ""
    rev_list = []
    y = 1
    for e in data_list:
        rev_list.append(data_list[-y])
        y += 1
    reversed_list = []
    for s in rev_list:
        for n in s:
            reversed_list.append(int(n))
    return reversed_list