import re

# Change name of result file
save_as = open("Margaret Atwood - Oryx And Crake.txt", 'w', encoding='utf8')

#Change the name of source file
with open('Atwood-Margaret-Oryx-And-Crake.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        #Change the regex to what you want to delete
        l = re.sub(r'~', r'', l)
        l = re.sub(r'(\d)*', r'', l)
        l = re.sub(r'“', r'"', l)
        save_as.write(l)

