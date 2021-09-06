def presses(phrase):
    keypad = ['1','ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6','PQRS7','TUV8','WXYZ9',' 0','*','#']
    position = 0
    phrase = phrase.upper()
    for letter in phrase:
        for key in keypad:
            if letter in key:
                for click in key:
                    position += 1
                    if letter == click:
                        break
    return(position)