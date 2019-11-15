# Variables having same memory address  (is) (is not)

# Variables having same data irrespective of memory address (==) (!=)

print('-----------variable equality-----------------')
print('----------immutable objects------------------')
a = 10
b = 10  # python will have same shared memory address for a and b as they are immutable objects

print('{0} , {1}'.format(id(a), id(b)))
print("a is b", a is b)
print("a == b", a == b)

print('---------- reassigning a and b------------------')
a = 500
b = 500
print('id of a and b: ', id(a), id(b))
print("a is b", a is b)
print("a == b", a == b)

print('---------- int and float-----------------')

a = 10
b = 10.0
print('id of a and b: ', id(a), id(b))
print("a is b", a is b) # dont share same memory address
print("a == b", a == b) # logically 10 and 10.0 is same

print('----------complex number-----------------')

a = 10 + 0j
b = 10.0
print("type of variable a: ",  type(a))
print('id of a and b: ', id(a), id(b))
print("a is b", a is b) # dont share same memory address
print("a == b", a == b) # logically 10 and 10.0 is same


print('----------mutable objects------------------')
a = [1, 2, 3] # 2 identical list will not have shared references as they are mutable and hence a is b will be false
b = [1, 2, 3]
print('id of a and b: ', id(a), id(b))
print("a is b", a is b)
print("a == b", a == b)

print('----------None object------------------')

print("id of None", id(None))
print("Type of None", type(None))
a = None
b = None
print('id of a and b: ', id(a), id(b))
print("a is b", a is b)
print("a == b", a == b)
print("a is None", a is None)
print("a is Not None", a is not None)
print("Not(a is None)", not(a is None))






