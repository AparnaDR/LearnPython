# #### SHared references with immutable objects
# Shared Reference is the concept when two variables are referring to the same memory address
print('------------shared references in mutable and immutable objects----------------')

print('------------immutable variable----------------')
a = 10
b = a
print(id(a))
print(id(b))  # will point to same memory address as 'a', its not creating new memory and not copying the value

print('------------immutable function----------------')
# functions
def my_func(v):  # v and c variables are referring to the same memory address which contains the number 11
    print(id(v))


c = 11
print(id(c))
my_func(c)
print('----------------------------')
# if two variables contain same value, both variables are pointing to the same memory address
print('----------------------------')
a1 = 100
b1 = 100
print(id(a1))
print(id(b1))

print('-----------immutable string-----------------')
a2 = 'hello'
b2 = 'hello'
print(id(a2))
print(id(b2))
b2 = 'hello world'
print(id(a2))
print(id(b2))
print('-----------mutable list-----------------')
# #### SHared references with mutable objects
# With mutable objects like list, python will never create shared references even though list is equal

a = [1, 2, 3]
b = [1, 2, 3]

print('{0}, {1}'.format(id(a), format(id(b))))
c = b  # b and c shares same memory address
print('{0}, {1} , {2}'.format(id(a), id(b), id(c)))
b.append(100)
print('{0}, {1} , {2}'.format(a, b, c))
print('{0}, {1} , {2}'.format(id(a), id(b), id(c)))

print('----------------------------')