a = [1, 2, 3]

a = [1,  # item1
     2, 3
    , 4]
b = (1,  # item1
     2,
     3, 4)


def my_fuc(a,  # this is a
           b,
           c):
    print(a)


my_fuc(10,  # a value
       11
       , 12)

# You can break up statements over multiple lines explicitly, by using the \ (backslash ) character
a = 10
b = 11
c = 12
if a > 5 \
        and b > 10 \
        and c > 20:
    print('ok')


# triple delimiter
# Multi-line string literals can be created using triple delimiters (' single or " double)
a = """ today
i am
doing
multi line strings chapter
!!!

sdfdf
"""
print(a)