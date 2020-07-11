fpath = 'C:/Users/Administrator/Desktop/[PRP201]/Resources/'
# fname = 'romeo.txt'
fname = 'mbox-short.txt'

try:
    fhand = open(fpath+fname)
except :
    print('File cant be opened:', fname)
    quit()

# lst = list()                       # list for the desired output
# for line in fhand:                    # to read every line of file romeo.txt
#     word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
#     for element in word:           # check every element in word    
#         if element in lst:         # if element is repeated
#             continue               # do nothing
#         else :                     # else if element is not in the list
#             lst.append(element)    # append     
# lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
# print(lst)                          # print the list
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    print(email)     
    count += 1
print("There were", count, "lines in the file with From as the first word")






