def kebabize(string):
    kebab_string = ""
    first = 1
    for letter in string:
        if letter.isalpha():
            if letter.isupper():
                if first == 1:
                    kebab_string += letter.lower()
                else:
                    kebab_string = kebab_string + "-" + letter.lower()
            else:
                kebab_string += letter
            first += 1
    return kebab_string