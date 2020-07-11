import re

fname = 'regex_sum_581872.txt'
fpath = '/Users/vtt/Desktop/[PRP201]_Python.MOOC/Resources/'
fhandle = open(fpath+fname)

# numblist = list()
x = list()
for line in fhandle:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    x = x+y

sum=0
for z in x:
    sum = sum + int(z)
print(sum)

