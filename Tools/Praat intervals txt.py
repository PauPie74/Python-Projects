import re

files = ['Banksy', 'C_Leonardo', 'C_Ryman', 'C_Twombly', 'C_Warhol', 'S_Boticelli', 'S_Monet']
file_in = input("file name: ")

def convert(file_in):
  file_name = file_in + '.txt'

  with open(file_name, 'r') as file :
    filedata = file.read()

  # Replace the target string
  filedata = filedata.replace(' ', '')
  filedata = filedata.replace('\n', '')
  filedata = filedata.replace('intervals', '\n')
  filedata = filedata.replace(':', ';')
  filedata = filedata.replace('xmin=', '')
  filedata = filedata.replace('xmax=', ';')
  filedata = filedata.replace('text=', ';')

  # Write the file out again
  new_file = file_in + ' 2.txt'

  with open(new_file, 'w') as file:
    file.write(filedata)

# open_file = open(file, 'r')
#
# output_file = 'output.txt'
# save_as = open(output_file, 'w')
#
#
# line = open_file.replace("\s","")
# # line = re.sub(r'\s', '', open_file)
# # line = re.sub(r'\n', '', open_file)
#
# print(line)
#
# # for line in open_file:
# #     # new_line = re.sub(r'intervals \[[\d]*\]:[\n|\s]*xmin = ([\d]*[\.]*[\d]*)[\n|\s]*xmax = ([\d]*[\.]*[\d]*)[\n|\s]*text = \"([\w]*)\"','c',line)
# #
# #     # line = re.sub(r'intervals \[[\d]*\]:','\n',line)
# #     print(line)

for name in files:
  convert(name)
