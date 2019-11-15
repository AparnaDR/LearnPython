import sys
import time

# Integers in Python
#  0 ,10 , -100
# Integers are objects
"""
use 32 bits to store (signed) integers, our range would be:
2(32-1) = 231 = 2,147,483,648 Range: [-2,147,483,648 … 2,147,483,647]
"""

print(type(100))  # will return the class integer

# To find out how much memory is used to store a particular number
# for 64 bit processor and 32 bit processor the output will be different
print(sys.getsizeof(0))  # 12
print(sys.getsizeof(1))  # 14
print(sys.getsizeof(2 ** 100))
print(2 ** 100)

# operations in integers

