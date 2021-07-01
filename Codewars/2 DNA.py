import re

def DNA_strand(dna):
    x = re.sub(r'A','X',dna)
    x = re.sub(r'T','Y',x)
    x = re.sub(r'X','T',x)
    x = re.sub(r'Y','A',x)
    x = re.sub(r'C','X',x)
    x = re.sub(r'G','Y',x)
    x = re.sub(r'X','G',x)
    x = re.sub(r'Y','C',x)
    return x