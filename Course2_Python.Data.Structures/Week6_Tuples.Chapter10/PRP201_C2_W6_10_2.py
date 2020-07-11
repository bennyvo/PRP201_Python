fname = 'mbox-short.txt'
fpath = 'C:/Users/Admin/Desktop/[PRP201] Python.MOOC/Resources/'
fhandle = open(fpath+fname)

counts = dict()
#read file
for line in fhandle:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    hrs = words[5].split(':')
    counts[hrs[0]] = counts.get(hrs[0],0)+1

    # hr = hrs[0]
    # counts[hr] = counts.get(hr,0)+1

    #Count words
    # for word in words:
    #     counts[word] = counts.get(word,0) + 1
# print(sorted([(v,k) for k,v in counts.items()]))
# lst = list()

# for k,v in counts.items():
#     newtuples = (v,k)
#     lst.append(newtuples)
    
# lst.sorted(lst)
# #Print-out
# for v,k in lst:
#     print(k,v)

for k in sorted(counts):
    print(k,str(counts[k]))