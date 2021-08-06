def wave(people):
    final_wave = []
    n = 0
    x = 0
    l = len(people)
    if l > 0:
        last = -1
        while people[last] == " ":
            l -= 1
            last -= 1
    while n < l:
        letter_wave = ""
        x = 0
        for letter in people:
            if n == x:
                if letter != " ":
                    letter_wave += letter.upper()
                else:
                    letter_wave += " "
                    n += 1
            else:
                letter_wave += letter
            x += 1
        final_wave.append(letter_wave)
        n += 1
    return final_wave