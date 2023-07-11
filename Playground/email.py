import re

i = input()

email = '[a-zA-Z0-9_-]*@[a-z]*\.[a-z]*'

if re.search(email,i):
    print('TAK')
else:
    print('NIE')