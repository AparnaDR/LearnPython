"""
a = 10
print(hex(id(a)))

a = 15  # 10 and 15 are in different memory locations
# In fact, the value inside the int objects, can never be changed!
print(hex(id(a)))

a = a + 15
print(hex(id(a)))
# even if we add it will store in different location

# Numbers,Strings,Tuples, frozen sets, user defined classes( user can or cannot allow )
# are immutable ( values cannot be changed)
# Lists, Sets, Dictionaries,user defined classes  are mutable

# Tuple containing a list
#  List values can be modified but not the tuple itself

a = [1, 2]
b = [3, 4]
tup = (a, b)
print(tup)
print(id(tup))
a.append(3)  # list can be appended , but not tuple
b.append(5)
print(tup)
print(id(tup))
tup[0].append(11)
tup[1].append(12)
print(tup)
print(id(tup))


# List
my_list_1 = [1, 2, 3]
print(my_list_1)
print(id(my_list_1))

my_list_1.append(4)
print(my_list_1)
print(id(my_list_1))  # memory address is not changed after appending

my_list_1 = my_list_1 + [5]
print(my_list_1)
print(id(my_list_1))  # memory address is changed , as it first evaluates right hand side and to store
# that memory is created

#  Dictionaries

my_dict = dict(key1=1, key2='val2')
print(my_dict)
print(id(my_dict))

my_dict['key3'] = 10.3
print(id(my_dict))  # memory address is not changed after appending




#  variables mutability within a function
# String in function - Strings are immutable


def process(s):  # s is still pointing to same memory as of mu_var
    print('Initial s # = {0}'.format(id(s)))
    s = s + 'world'  # now a new object is created with new memory address and now is s is referenced there
    print('Final s # = {0}'.format(id(s)))


my_var = 'hello'
print('Initial my_var # = {0}'.format(id(my_var)))
process(my_var)
print('Final my_var # = {0}'.format(id(my_var)))  # my_var value will not be changed as it is still pointing to hello
print('my_var = {0}'.format(my_var))


# list , mutable object
def modify_lst(lst): # same memory address is sent here
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100) # as list is an mutable object, when appended memory address will not be changed and reference
    # also will not be changed
    print('Final lst # = {0}'.format(id(lst)))


my_lst = [1, 2, 3]
print(id(my_lst)) # memory add of list
modify_lst(my_lst) # the same reference is passed to the function
print(my_lst)

"""

# tuple - immutable object, contents may be mutable


def modify_tuple(t): # same memory address is sent here
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100) # as tuple is an immutable object, when appended memory address will not be changed and reference
    # also will not be changed
    print('Final t # = {0}'.format(id(t)))


my_tuple = ([1, 2, 3], 'a')
print(id(my_tuple)) # memory add of list
modify_tuple(my_tuple) # the same reference is passed to the function
print(my_tuple)