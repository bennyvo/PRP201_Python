# n=5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Done')
# print(n)


# friends = ['An', 'Hung', 'Long', 'Khiem']
# for friend in friends:
#     print('Hello:', friend)
# print('For loop done!')


# smallest_so_far = -1
# expression_list = [9, 41, 12, 3, 74, 15]
# print('Before', smallest_so_far)
# for the_num in expression_list:
#     if the_num > smallest_so_far:
#         smallest_so_far = the_num
#     print('Tmp largest numb:',smallest_so_far, 'Tmp current numb', the_num)
# print('After all, the largest numb', smallest_so_far)


# count = 0
# sum = 0
# list = [9,41,12,3,74,15]
# print('Before', count, sum)
# for value in list:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum/count)


# print('Before')
# list = [9,41,12,3,74,15,99]
# for value in list:
#     if value > 20:
#         print('Number larger than 20:', value)
# print('After')

# found = False
# print('Before',found)
# list = [9,41,12,3,74,15,99]
# for value in list:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)


# smallest_so_far = None
# expression_list = [9, 41, 12, 3, 74, 15]
# print('Before', smallest_so_far)
# for the_num in expression_list:
#     if smallest_so_far is None:
#         smallest_so_far = the_num
#     elif the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print('Tmp smallest numb:',smallest_so_far, 'Tmp current numb', the_num)
# print('After all, the largest numb', smallest_so_far)



#Ex_05_01
# numb = 0
# total = 0.0

# while True:
#     sVal = input('Enter number:')
#     if sVal == 'done':
#         break
#     try:
#         fVal = float(sVal)
#     except :
#         print('Invalid Input')
#         continue    
#     print(fVal)
#     numb = numb + 1
#     total = total + fVal

# print('All Done!')
# print(total,numb, total/numb)


largest = None
smallest = None
while True:
    num = input('Enter number: ')
    if num == "done" : break
    try:
        num = int(num)
    except :
        print('Invalid Input')
        continue 
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)

# smallest_so_far = -1
# expression_list = [9, 41, 12, 3, 74, 15]
# print('Before', smallest_so_far)
# for the_num in expression_list:
#     if the_num > smallest_so_far:
#         smallest_so_far = the_num
#     print('Tmp largest numb:',smallest_so_far, 'Tmp current numb', the_num)
# print('After all, the largest numb', smallest_so_far)

# smallest_so_far = None
# expression_list = [9, 41, 12, 3, 74, 15]
# print('Before', smallest_so_far)
# for the_num in expression_list:
#     if smallest_so_far is None:
#         smallest_so_far = the_num
#     elif the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print('Tmp smallest numb:',smallest_so_far, 'Tmp current numb', the_num)
# print('After all, the largest numb', smallest_so_far)
