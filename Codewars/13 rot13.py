def rot13(message):
    exclude = '''!@#$%^&*()_-+={}[];:"'<>,./?~`\| 1234567890'''
    str = ""
    for letter in message:
        letter_num = ord(letter) + 13
        if letter in exclude:
            str += letter
        else:
            if letter.isupper():
                if letter_num > 90:
                    letter_num -= 26
            elif letter.islower() == True:
                    if letter_num > 122:
                        letter_num -= 26
            str += chr(letter_num)
    return str