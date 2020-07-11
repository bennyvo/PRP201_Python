# fhand = open('C:/Users/Administrator/Desktop/[PRP201]/mbox-short.txt',mode='r', encoding='utf-8')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line count:', count)

# fhand = open('C:/Users/Administrator/Desktop/[PRP201]/mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])
# count = 0
# for line in fhand:
#     line = line.strip()
    # if line.startswith('From:'):
    #     print(line)
    # if not line.startswith('From:'):
    #     continue   
    # print(line)
    # if not '@uct.ac.za' in line:
    #     continue   
    # print(line)
#     if line.startswith('Subject:'):
#         count = count + 1   
# print('There were', count, 'subject line in')

fpath = 'C:/Users/Administrator/Desktop/[PRP201]/'
fname = input('Enter file name:')
count = 0

try:
    fhand = open(fpath+fname)
except :
    print('File cant be opened:', fname)
    quit()

for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject line in', fname)      


