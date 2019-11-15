"""
names  = ['aparna','archana','maheshwari','ramanakumar']
print(names)
print(names[2:])
print(names[1])
print(names[-1])
names[0] = 'Aparna'
print(names)
# names.append('Likitha','Pragya') error only one object cab be added
names.append(['Likitha','Pragya'])
print(names)
print(names[:]) # all names

numbers = [4, 11, 5, 3, 15, 2, 9]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print(largest)

#List Methods
#insert

lista = [2,3,4,56,7]
lista.insert(0,1)
print(lista)

#remove
lista.remove(56)
print(lista)

#clear
lista.clear()
print(lista)

#pop - remove last item in a list
listb = [2,3,4,56,7]
listb.pop()
print(listb)

#index - to check for index of an item
listb = [2,3,4,56,7,7,7]
print(listb.index(56))

#in - to check for existence in a list
print(33 in listb)

# count occurrences in a list
print(listb.count(7))

#sort and reverse
listc = [2,3,4,56,7,7,7]
listc.sort()
print(listc)
listc.reverse()
print(listc)

# copy
listd = listc.copy()
print(listd)

# add new object to original list, should not affect copied list
listc.append(99)
print(listc)
print(listd)
"""
# program to remove duplicates in a list
liste = [2,3,4,56,7,7,7,3,2,1,5,8,9,6,9,7]
uniquelist = []
for item in liste:
    if item not in uniquelist:
        uniquelist.append(item)
print(uniquelist)


