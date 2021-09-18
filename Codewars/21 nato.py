def to_nato(words):
    nato =  {
        'A': 'Alfa',  'B': 'Bravo',   'C': 'Charlie',
        'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
        'G': 'Golf',   'H': 'Hotel',   'I': 'India',
        'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
        'M': 'Mike',   'N': 'November','O': 'Oscar',
        'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'}
    punct = ",.!?"
    words = words.upper()
    nato_string = ""
    for letter in words:
        if letter in punct:
            nato_string += letter + " "
        elif letter == " ":
            nato_string += ""
        else:
            nato_string += nato[str(letter)] + " "
    nato_string = nato_string[:-1]
    return nato_string