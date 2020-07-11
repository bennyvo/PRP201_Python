# d = {'a':10,'b':1, 'c':22}
# t = sorted(d.items())
# print(t)
# for k, v in sorted(d.items()):
#     print(k,v)

# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items():
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

fname = 'romeo.txt'
fpath = '/Users/vtt/Desktop/[PRP201]_Python.MOOC/Resources/'
fhandle = open(fpath+fname)

counts = dict()
#read file
for line in fhandle:
    words = line.split()
    #Count words
    for word in words:
        counts[word] = counts.get(word,0) + 1

# lst = list()

# for k,v in counts.items():
#     newtuples = (v,k)
#     lst.append(newtuples)
# lst = sorted(lst, reverse=True)
# #Print-out
# for v,k in lst[:10]:
#     print(k,v)
print(sorted([(v,k) for k,v in counts.items()]))


