fname = 'mbox-short.txt'
fpath = 'C:/Users/Admin/Desktop/[PRP201]/'

fhandle = open(fpath+fname)
maxauthor = dict()

for line in fhandle:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    maxauthor[words[1]] = maxauthor.get(words[1], 0) + 1
largest = None
largest_author = None

# for key in maxauthor:
#     if largest is None: largest = maxauthor[key]
#     if largest < maxauthor[key]:
#         largest = maxauthor[key]
#         largest_author = key

for key,value in maxauthor.items():
    if largest is None or value > largest:
        largest = value
        largest_author = key

print(largest_author,largest)