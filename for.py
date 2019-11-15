"""
for item in 'Python':
    print(item)

# list
for item in ['Aparna','Sandesh','Pragya','Aparna']:
    print(item)

# tuple
for item in ('a','b','c','d'):
    print(item)


# range
for item in range(5):
    print(item)

for item in range(500,510):
    print(item)

# range with index
for item in range(600,610,3):
    print(item)

# exercise 1
# total of all prices

cart_prices = [100,200,300]
total = 0

for price in cart_prices:
    total = total+price
print(total)



# nested loops
# print co ordinates for a range of 3 ,2

for x in range(3):
    for y in range(2):
        print(f"({x} , {y})")



# print letter F using numbers
# answer 1
numbers = [5,2,5,2,2]
for item in numbers:
    print('x' * item)



# answer 2

numbers = [5,2,5,2,2]
for item in numbers:
    output = ''
    for x in range(item):
        output += 'x'
    print(output)

# print letter L on console
numbers = [2,2,2,2,5]
for item in numbers:
    output = ''
    for x in range(item):
        output += 'x'
    print(output)

# In python, an iterable is an object capable of returning values one at a time

# print each list which contains tuples
for i , j in [(1,2),(3,4),(4,5)]:
    print(i, j)

for i in [(1, 2), (3, 4), (4, 5)]:
    print(i)

# continue statement in for loop
# print numbers from 1 to 5 except for number 3


for i in range(5):
    if i == 3:
        continue
    print(i)

# break statement in for loop
# print numbers from 1 to 5, break the loop when number has 3

for i in range(5):
    if i == 3:
        break
    print(i)

# else in for
# program  - break the loop when multiple of 7 is found in a range of 1 to 10
# try with range 1 to 10 and 1 to 5
for i in range(1, 10):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('multiple of 7 not found')


# for - continue within try
# program to print division by zero error in a range 1 to 5 when i is 10/3-3
# finally will run irrespective of break or continue is there
# with continue the loop doesnt break when it encounters division by 0
# with break loop breaks when it encounters division by zero error

for i in range(5):
    print('----------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('divided by zero')
        continue
    finally:
        print('always run')
    print(i)
"""

# enumarate in for
# gets the index

for i , c in enumerate('hello'):
    print(i , c)



