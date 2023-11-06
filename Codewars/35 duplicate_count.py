def duplicate_count(text):
    text = list(text.lower())
    doubles = 0
    x = 0
    while x < len(text):
        l = text[x]
        text.pop(0)
        if l in text:
            doubles += 1
            while l in text:
                text.remove(l)
    return doubles