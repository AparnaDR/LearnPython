# creating our own reducing funs, which will work only on sequences but in general pythons reducing fn works on any
# iterable

l = [5, 6, 7, 4, 3, 9]

print(' reducing fun to find maximum num in a sequence')
print(l)
maximum = lambda x, y: x if x > y else y


def max_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = maximum(result, x)
    return result


print(max_seq(l))

print(' reducing fun to find minimum num in a sequence')
print(l)

minimum = lambda x, y: x if x < y else y


def min_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = minimum(result, x)
    return result


print(min_seq(l))

print(' reducing fun to find addition of all num in a sequence')
print(l)

addition = lambda x, y: x + y


def add_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = addition(result, x)
    return result


print(add_seq(l))


# if you notice above 3 funs are same so lets write a generic fun

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print('------using customized reduce fun-----------')
print(l)
print('max: ', _reduce(maximum, l))
print('min: ', _reduce(minimum, l))
print('add: ', _reduce(addition, l))

# above will work only on sequence like list, wont work for set which doesnt have indexing
# we can use pythons inbuilt reduce fun

from functools import reduce

print('------using pythons reduce fun-----------')
print(l)
print('max: ', reduce(maximum, l))
print('min: ', reduce(minimum, l))
print({1, 2, 3, 4, 5})
print('add: ', reduce(addition, {1, 2, 3, 4, 5}))

# we can also use the min, max and add functions
print('------using min, max and sum functions-----------')
print(min(l))
print(max(l))
print((sum(l)))
# we can use any iterable like set list anything on pythons function

# all function -- does a 'and' of all the elements, if all are true then the out put is true else false
# any function -- does a 'or' of all the elements, if any 1 is true then the out put is true else false

s = [True, 1, 0, None]
print(s)
print('all: ', all(s))  # False, if all are true it will return true else false
print('any:', (any(s)))  # true , if any 1 is true it will return true else false

# product of elements

print('product of elements using reduce fun')
l = [5, 6, 7, 4, 3, 9]

res = reduce(lambda x, y: x * y , l)
print(res)

# n! = 1 * 2 * 3 * 4... * n
print('factorial of 5 using reduce fun')
print(range(5))
print(list(range(5))) #  we are getting the range with 0, we need to remove that
print(list(range(1, 5+1))) # we are starting from 1 to n+1
res = reduce(lambda x, y: x * y, list(range(1, 5+1)))
print(res)  # factorial of 5! = 120

# lets write a function to generalize n

print('--------------------------')
def fact(n):
    return reduce(lambda x, y: x * y, list(range(1, n+1)))

print(fact(5))



print('factorial of 5 using recursive fun')

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(5))

#  generalize our _reduce fun to accept any sequences

def _reduce(fn, sequence, initial):
    result = initial # initial is what we pass in the function, if we pass 100 results initial value will be 100
    for x in sequence:
        result = fn(result, x)
    return result

print('============================')
l = [1, 2, 3, 4]

# sum of all numbers
print(_reduce(lambda a, b: a+b, l, 0))
# product of all numbers
print(_reduce(lambda a, b: a*b, l, 1))
# maximum of all numbers
print(_reduce(lambda a, b: a if a > b else b, l, 0))
# minium of all numbers
print(_reduce(lambda a, b: a if a < b else b, l, 0))
# factorial of all numbers
print(_reduce(lambda a, b: a * b , l, 1))
# addition using a set with initial value as 100
# sum of all numbers
print(_reduce(lambda a, b: a+b, {5, 50 , 40, 10}, 100))



