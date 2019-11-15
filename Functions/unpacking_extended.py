# slicing
# works only which are indexable, for example we cannot slice sets as its not oderable

print('-------slicing----------')
l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
print(a)
print('----')
print(b)

# below is another and better way to do the same
# unpacking using starred expressions
# starred expressions always retun a list
# works on any iterable
print('********************************')
print('------unpack using starred exp on LHS-------')
print('********************************')
print('-------unpacking list using starred expressions----------')
l = [1, 2, 3, 4, 5, 6]
a, *b = l
print(a)
print('----')
print(b)

print('-------unpacking string using starred expressions----------')
s = 'python'
a, *b = s  # returns a list
print(a)
print('----')
print(b)

print('-------unpacking tuple using starred expressions----------')
tup = (1, 2, 3, 4, 5, 6)
a, *b, c = tup  # returns a list
print(a)
print('----')
print(b)
print('----')
print(c)

print('-----slicing returns string----')

s = 'python'

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print('----')
print(b)
print('----')
print(c)
print('----')
print(d)

print('-----slicing to return list using starred exp----')
s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
*c, = c  # starred exp will return list
print(a)
print('----')
print(b)
print('----')
print(c)
print('----')
print(d)

print('-----slicing to return list using list constructor----')
s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print('----')
print(b)
print('----')
print(list(c))
print('----')
print(d)

print('----unpacking set to a list using list constructor---')
s = {'a', -100, 2.344, 77, 'a'}
li = list(s)
print(li)

print('----unpacking set to a list using starred expr---')
s = {'a', -100, 2.344, 77, 'a'}
*c, = s
print(c)

print('********************************')
print('------pack using starred exp on RHS-------')
print('********************************')

print('------unpack list--------')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

print('------unpack list and string--------')
l1 = [1, 2, 3]
l2 = 'abc'
l = [*l1, *l2]
print(l)

print('------unpack list and set--------')
l1 = [1, 2, 3]
s2 = {'a', 'b', 'c'}
l = [*l1, *s2]
print(l)

print('------unpack list and set--------')
l1 = [1, 2, 3]
s2 = {'a', 'b', 'c'}
l = [*l1, *s2]
print(l)

print('------unpack 2 strings which have repeated item to a list--------')
s1 = 'abc'
s2 = 'cad'
l = [*s1, *s2]  # list can have duplicate values
print(l)

print('------unpack 2 strings which have repeated item to a set--------')
s1 = 'abc'
s2 = 'cad'
l = {*s1, *s2}  # sets cannot have duplicate values
print(l)

print('------unpack 2 sets which have repeated item to a set--------')
s1 = {1, 2, 3}
s2 = {3, 4, 5}
l = {*s1, *s2}  # sets cannot have duplicate values
print(l)

# we can also use union operator to join sets, but it will always return set
print(s1.union(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {6, 21, 31}
s4 = {31, 42, 53}
print(s1.union(s2.union(s3.union(s4))))  # returns set
print(s1.union(s2, s3, s4))  # returns set
print([*s1, *s2, *s3, *s4])  # returns list with duplicate values
print((*s1, *s2, *s3, *s4))  # returns list without duplicate values

print('------unpack 2 dicts which have repeated key--------')
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 22, 'key3': 3}

print('------unpack keys--------')
print({*d1, *d2})  # will unpack only keys into a set(no repeated keys)(no order will be maintained)

print('------unpack keys and values--------')
print({**d1, **d2})

print('------ add additional values and then unpack keys and values--------')
print({'a': 1, 'b': 2, **d1, **d2})

print('------nested unpacking--------')
a, b, (c, d) = [1, 2, 'XY']
print(a, b, c, d)

a, b, (c, d, *e) = [1, 2, 'python']
print(a, b, c, d, e)

print('------unpacking using slicing--------')
l = [1, 2, 3, 4, 'python']
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)




