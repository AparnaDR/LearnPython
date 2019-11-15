# tuples are similar to list, unlike list we cannot add, remove items form tuple. they ate immutable,cannot change them
# no append,remove, clear,insert,pop
# only count and index methods are available
# we can only get information of a tuple but not change it
numbers =(1,2,3)
print(numbers.count(1))
# numbers[0] = 10 # error
print(numbers[0])

# unpackaging
coordinates=(1,2,3)
"""
x = coordinates[0]
y = coordinates[1]
z = coordinates[2] """

# above 3 lines of code can also be written like below
# shorthand
# we are unpacking tuple in to a variable
# takes first item in the tuple and assign it to a variable
# coordinate 1 will be assigned to x
x,y,z = coordinates

print(x)

# unpacking is applicable to list also

