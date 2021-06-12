import re

punc = '''!@#$%^&*()_-+={}[];:"'<>,./?~`\| '''

### Morse
# Morse dictionary
morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.','0':'-----','\n':'\n','':''}

# Morse encrypt functions
def encrypt_morse():
    for line in input_text:
        text = line
        result = encrypt_morse_letter(text.upper())
        save_as.write(result)

def encrypt_morse_letter(text):
    cipher = ''
    for letter in text:
        if letter == ' ':
            cipher += ' '
        if letter not in punc:
            if letter != ' ':
                cipher += morse_code[letter] + ' '
            elif letter not in morse_code:
                cipher += ' '
            else:
                cipher += ' '
    return cipher

# Morse decrypt functions
def decrypt_morse():
    for line in input_text:
        text = line
        result = decrypt_morse_letter(text)
        save_as.write(result)

def decrypt_morse_letter(text):
    text += ' '
    decipher = ''
    citext = ''
    s = 0
    for letter in text:
        if letter != ' ':
            s = 0
            citext += letter
        else:
            s += 1
            if s == 2:
                decipher += ' '
            else:
                decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
                citext = ''
    return decipher

### Caesar
def caesar_encrypt():
    for line in input_text:
        for letter in line:
            letter_num = ord(letter)+3
            if letter in punc:
                save_as.write(letter)
            else:
                if letter.isupper() == True:
                    if letter_num > 90:
                        letter_num -= 26
                elif letter.islower() == True:
                    if letter_num > 122:
                        letter_num -= 26
                c_letter = chr(letter_num)
                save_as.write(str(c_letter))

def caesar_decrypt():
    for line in input_text:
        for letter in line:
            letter_num = ord(letter)-3
            if letter in punc:
                save_as.write(letter)
            elif letter == '\n':
                save_as.write(letter)
            else:
                if letter.isupper() == True:
                    if letter_num < 65:
                        letter_num += 26
                elif letter.islower() == True:
                    if letter_num < 97:
                        letter_num += 26
                c_letter = chr(letter_num)
                save_as.write(str(c_letter))

#### Affine

# Affine encrypt
def affine_dic_create(a: int, b: int)  -> None:
    affine_dic = dict()
    for i in range(26):
        key = chr(i+ord('A'))
        affine_dic[key] = chr(((a*i+b)%26)+ord('A'))
    for i in range(26):
        key = chr(i+ord('a'))
        affine_dic[key] = chr(((a*i+b)%26)+ord('a'))
    affine_dic['\n'] = '\n'
    affine_dic[' '] = ' '
    return affine_dic

def encrypt_affine():
    a = int(input('Type a: '))
    b = int(input('Type b: '))
    affine_dic = affine_dic_create(a,b)
    for line in input_text:
        text = line
        result = encrypt_affine_letter(text, affine_dic)
        save_as.write(result)

def encrypt_affine_letter(text,affine_dic):
    cipher = ''
    for letter in text:
        if letter not in affine_dic:
            cipher += letter
        elif letter != ' ':
            cipher += affine_dic[letter]
        else:
            cipher += ' '
    return cipher

# Affine decrypt
def affine_dic_create_decrypt(a: int, b: int) -> None:
    affine_dic_dec = dict()
    for i in range(26):
        key = chr(((a*i+b)%26)+ord('A'))
        affine_dic_dec[key] = chr(i+ord('A'))
    for i in range(26):
        key = chr(((a*i+b)%26)+ord('a'))
        affine_dic_dec[key] = chr(i+ord('a'))
    affine_dic_dec['\n'] = '\n'
    affine_dic_dec[' '] = ' '
    return affine_dic_dec

def decrypt_affine():
    a = int(input('Type a: '))
    b = int(input('Type b: '))
    affine_dic = affine_dic_create_decrypt(a,b)
    for line in input_text:
        text = line
        result = decrypt_affine_letter(text,affine_dic)
        save_as.write(str(result))

def decrypt_affine_letter(text,affine_dic):
    cipher = ''
    for letter in text:
        if letter not in affine_dic:
            cipher += letter
        elif letter != ' ':
            cipher += affine_dic[letter]
        else:
            cipher += ' '
    return cipher

### URL

# URL dictionary
url_dic = {'%':'%25',':':'%3a','/':'%2f','?':'%3f','#':'%23','[':'%5b',']':'%5d','@':'%40','!':'%21','$':'%24','&':'%26',
           '\'':'%27','(':'%28',')':'%29','*':'%2a','+':'%2b',',':'%2c',';':'%3b','=':'%3d',' ':'%20'}

# URL encrypt
def encrypt_url():
    for line in input_text:
        text = line
        for letter in text:
            if letter in url_dic:
                save_as.write(url_dic[letter])
            else:
                save_as.write(letter)

# URL decrypt
def decrypt_url():
    for line in input_text:
        text = line
        result = decrypt_url_key(text)
        save_as.write(str(result))

def decrypt_url_key(text):
    for key in url_dic:
        url_decrypted = re.sub(url_dic[key],key,text)
        text = url_decrypted
    return url_decrypted

def done():
    print(32 * '*')
    print('*             DONE             *')
    print(32 * '*')

def error():
    print("")
    print(32 * '#')
    print("#            ERROR             #")
    print("#         Wrong value.         #")
    print(32 * '#')
    print("")
    main()

def open_f(file):
    file = input("Type the path and/or name of the file (with extension): ")
    try:
        open_file = open(file, 'r')
    except IOError:
        print("")
        print(32 * '#')
        print("#            ERROR             #")
        print("#    Can not find the file.    #")
        print(32 * '#')
        print("")
        open_file = open_f(file)
    return open_file

### Main
def main():
    print('Type to choose: \n 1 -- encrypt \n 2 -- decrypt')
    chosen = input()
    print(32 * '*')
    if chosen == '1':
        print('Type to choose: \n 1 -- Morse \n 2 -- Caesar \n 3 -- Affine \n 4 -- URL')
        chosen_cipher = input()
        if chosen_cipher == '1':
            # Morse encrypt
            encrypt_morse()
            done()
        elif chosen_cipher == '2':
            # Caesar encrypt
            caesar_encrypt()
            done()
        elif chosen_cipher == '3':
            # Affine encrypt
            encrypt_affine()
            done()
        elif chosen_cipher == '4':
            # Url encrypt
            encrypt_url()
            done()
        else:
            error()
    elif chosen == '2':
        print('Type to choose: \n 1 -- Morse \n 2 -- Caesar \n 3 -- Affine \n 4 -- URL')
        chosen_cipher = input()
        if chosen_cipher == '1':
            # Morse decrypt
            decrypt_morse()
            done()
        elif chosen_cipher == '2':
            # Ceasar decrypt
            caesar_decrypt()
            done()
        elif chosen_cipher == '3':
            # Affine decrypt
            decrypt_affine()
            done()
        elif chosen_cipher == '4':
            # Url decrypt
            decrypt_url()
            done()
        else:
            error()
            main()
    else:
        error()


### Program starts here ###

print(32*'*')
print('*  Welcome to CIPHER DENcoder  *')
print('*           ver 1.00           *')
print(32*'*')
print('')

print('Do you want to load the file or type the text in the console? \n 1 -- load the file \n 2 -- type in the console')
file_or_text = input()
print(32 * '*')

if file_or_text == '1':
    file = ''
    input_text = open_f(file)

if file_or_text == '2':
    input_text = input()

output_file = input("Type name of the output file (with extension): ")
save_as = open(output_file, 'w')

print('')
print(32*'*')

main()

if file_or_text == '1':
    input_text.close()

save_as.close()