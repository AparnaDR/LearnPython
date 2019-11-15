#  sorting with lambda expns

help(sorted)
# Return a new list containing all items from the iterable in ascending order.

l = [1, 5, 4, 6, 7, 8, 0]  # l will not be modified it will return a new sortrd list

print(sorted(l))
print(l)

print('------sorting letters--------')
l = ['c', 'B', 'D', 'a']
print(sorted(l))  # sorting happens based on the ordinal number. The ordinal number for smaller letters are less
# compared to capital letters. So sorting happens accordingly
print(ord('c'))
print(ord('A'))

print('-------------sorting letters irrespective of caps/small letter--------------')

print(sorted(l, key=lambda s: s.upper()))

print('---------sorting dictionary------')
d = {'abc': 200, 'def': 300, 'ghi': 100}
print(sorted(d))  # sorts keys
print(sorted(d, key=lambda e: d[e]))  # sorts values

print('----------- sorting complex numbers------------')

e = [3+3j, 0, 1-1j, 3+0j]
# print(sorted(e))  # default sorting wont work for complex numbers
print(sorted(e, key= lambda c: (c.real) ** 2 + (c.imag) ** 2))

# if any of the type doesnt have ordering then we can associate a function to sort any element

l = ['aparnaz', 'Archanac', 'Likitha', 'Pragyab', 'Aparna']
print(sorted(l))  # will consider case based on ordinal number
print(sorted(l,key=lambda s: s[-1]))  # sorting based on last character, if 2 strings have same character as the last
# letter, then it will retian same order as in the input list
