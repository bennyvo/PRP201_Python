# friends = ['Joe', 'Ann', 'Liz', 'Wu', 'Zhang']

# for friend in friends:
#     print('Hello_1: ', friend)

# for i in range(len(friends)):
#     friend = friends[i]
#     print('Hello_2: ', friend)

# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = a + b
# print(c)
# print(a)

# t = [1,2,3,4,5,6,7,8,9,10]
# t= [0,1,2,3,4,5,6,7,8,9]
# print(t[1:3])
# print(t[:4])
# print(t[4:])
# print(t[:])


# Test: 3,9,5 -> avg=5.6666
# total = 0
# count = 0
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average: ', average)
# 
# numberlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numberlist.append(value)
# average = sum(numberlist)/len(numberlist)
# print('Average: ', average)

# tmpList = 'Hello my name is Vo Trung Tan and my student ID is SE62332'
# stuff = tmpList.split()
# print(stuff)
# print(len(stuff))
# print(stuff[3])

fpath = 'C:/Users/Administrator/Desktop/[PRP201]/'
fname = 'mbox-short.txt'

try:
    fhand = open(fpath+fname)
except :
    print('File cant be opened:', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    pdomain = email.split('@')
    domain = pdomain[1]
    print('Date found', words[2], 'in', fname)   
    print('Email found', email, 'in', fname)     
    print('Domain found', domain, 'in', fname)   





