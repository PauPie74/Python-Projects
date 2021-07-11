def solution1(number):
    list = []
    n = 0
    while n < number-3:
        n += 3
        list.append(n)
    n = 0
    while n < number-5:
        n += 5
        if n not in list:
            list.append(n)
    total = 0
    for element in range(0, len(list)):
        total = total + list[element]
    return total

def solution2(number):
    list = []
    for x in range(0, number):
        if x > 0 and x % 3 == 0 and x % 5 == 0:
            list.append(x)
        elif x > 0 and x % 3 == 0:
            list.append(x)
        elif x > 0 and x % 5 == 0:
            list.append(x)
        total = 0
        for element in range(0, len(list)):
            total = total + list[element]
    return total
