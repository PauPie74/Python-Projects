def up_array(arr):
    number = ''
    a = []
    if arr == []:
        return None
    for value in arr:
        if value < 0 or value >= 10:
            return None
        else:
            number += str(value)
    n = int(number) + 1
    for digit in str(n):
        a.append(int(digit))
    return a