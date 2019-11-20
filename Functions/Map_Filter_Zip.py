"""
Higher order functions
A function that takes a function as a parameter and/or returns a function as its return value
Example: sorted
map
filter

map(func, *iterables) will then return an iterator that calculates the
function applied to each element of the iterables

filter(func, iterable) will then return an iterator that contains all the
elements of the iterable for which the function called on it is Truthy
"""


# Map
def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


print(fact(3))

# Map function
results = map(fact, range(6))
print(results)  # it returns an iterator

for x in results:
    print(x)

print('---------- run it again-----')
for x in results:
    print(x)  # it wont display, so its always good to cast the map to list
# its an generator once you exhaust the map it wont go back, map calculates only while printing as it has calculated
# once it wont calculate again, we need to cast to list to do the same

print('---------- cast the map to list-----')
results = list(map(fact, range(6)))
print(results)  # it returns an list

print('--- add elements from 2 list and a tuple------')
l1 = [10, 20, 30, 40, 50]
l2 = [1, 2, 3]
l3 = (100, 200, 300, 400)

results = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(results)  # it will ignore 40 and 50 as it considers only shortest list and ignore the rest
# as soon as one of the list is exhausted the whole thing will stop

# the map gets calculated only when we are requesting an item
# for example, in below code we are passing 3 pos. arguments but lambda is taking only 2
# but it will not throw error if we execute the map function
# it will throw error only when we try to print items
# do not cast it to list to verify the scenario

results = map(lambda x, y: x + y, l1, l2, l3)  # lambda has only x and y but we are passing l1, l2, and l3
print(results)  # no error displayed when you run still this line of code

# if we run below line of code we will get error, the map gets calculated only when we are requesting an item
# for x in results:
#    print(x)


# filter
print('-------------filter function------------')
print('--------- print values which are divisible by 3 in the range of 25----------')

results = list(filter(lambda x: x % 3 == 0, range(25)))
print(results)

print('---- filter without function---')
print('---- program to filter falsey items and print only thruthy items from a list')
# all the false items will be filtered
# 1, 4.5, True = True
# 0, False, '', None = False
l1 = [1, 0, 4.5, 'a', '', None, True, False]
print('list items containing thruthy and falsey items :', l1)
results = list(filter(None, l1))
print('list filtering out the falsey items: ', results)

print('-------------zip function------------')
# Zip function allows you to combine 2 or more sequence types

l1 = [10, 20, 30, 40, 50]
l2 = (1, 2, 3)
l3 = 'python'

results = list(zip(l1, l2, l3))
print(results)

print('without casting to list to zip')
results = zip(l1, l2, l3)

print('using for')
for x in results:
    print(x)

print('---------- run it again-----')
for x in results:
    print(x)  # it wont display, so its always good to cast the zip to list
# its an generator once you exhaust the zip it wont go back, zip also calculates only while printing as it has
# calculated once, it wont calculate again, we need to cast to list to do the same

print('----- shortest one is considered')
print(list(zip(range(1000000), 'python')))

print('----------list comprehension---------')
print('calculate factorial')

results = [fact(n) for n in range(10)]
print(results)  # unlike map it calculate the results here itself and not while iterating
# map only points to the memory object if we print the results if its not casted to a list
print('------------------')

# if we use generator () then same issue as map
results = (fact(n) for n in range(10))
print(results) # --- will point to an memory object of generator
print('using for')
for x in results:
    print(x)

print('---------- run it again-----')
for x in results:
    print(x)  # it wont display, so its always good to cast to list
# its an generator once you exhaust the iterator it wont go back, this also calculates only while printing as it has
# calculated once, it wont calculate again, we need to cast to list to do the same
print('--------cast it to list----------')
results = list((fact(n) for n in range(10)))
print(results)

print(' add two elements from a list using list comp')
l1 = [10, 20, 30, 40, 50]
l2 = (1, 2, 3, 4)

results = [x+y for x, y in zip(l1, l2)] # zip only will give (10,1), (20,2) ect
print(results)

print(' filter above results only which are even using list comprehension ')
results = [x+y for x, y in zip(l1, l2) if (x+y)%2 == 0 ]
print(results)

