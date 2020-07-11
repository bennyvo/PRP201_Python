fpath = 'C:/Users/Administrator/Desktop/[PRP201]/'
# fname = input('Enter file name: ')
fname = 'words.txt'
try:
    fhand = open(fpath+fname)
except :
    print('File cant be opened:', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    # line = line.upper()
    print(line.upper())