def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nums = []
    s = " "
    for l in text:
        l = l.lower()
        if l in alphabet:
            l = alphabet.index(l) + 1
            nums.append(str(l))
    return s.join(nums)