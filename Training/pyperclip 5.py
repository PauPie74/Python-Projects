# https://pyperclip.readthedocs.io/en/latest/

import pyperclip

pyperclip.copy("Hello world")
pyperclip.paste()

copied = input()

print(copied)