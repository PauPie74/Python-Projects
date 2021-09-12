def count(s):
    points = 0
    for c in s:
        if c == "!":
            points += 2
        if c == "?":
            points += 3
    return points

def balance(left, right):
    left = count(left)
    right = count(right)
    if left > right:
        return "Left"
    elif right > left:
        return "Right"
    elif left == right:
        return "Balance"