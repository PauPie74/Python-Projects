def remove_smallest(numbers):
    num = []
    for n in numbers:
        num.append(n)
    try:
        num.pop(num.index(min(num)))
        return num
    except:
        num = numbers
        return num