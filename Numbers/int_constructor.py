import fractions

# AN integer is an object -- an instance of the int class
# we have 2 constructors in int calss
# int(x = 0) , int(x , base=10) . See help(int)

# ### Constructor with one argument
print(type(10))
# print(help(int))
# default value = 0

a = int()
print(a)

# floating numbers will be truncated
a = int(10.99999999)
print(a)

# boolean
a = int(True)
print(a)

# fractions

a = fractions.Fraction(22,7)
print(a)
print(float(a))
print(int(a))

# ### Constructor with two argument
# if we dont specify base default base is 10

print(int("101", 2))
print(int("FF", 16))
print(int("ff", 16))

# Base 10 is 0,1,2,3....9
# Base 11 is 0,1,2,3....9,A
# Base 12 is 0,1,2,3....9,A,B

# if we try to print B in base 11 we will get value error - invalid literal
# print(int("B", 11))

# Binary representation of base 10 numbers
print(bin(2))

# Octal representation of base 10 numbers
print(oct(2))

# Hex representation of base 10 numbers
print(hex(2))





