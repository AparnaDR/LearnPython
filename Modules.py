# modules is a file with some python code, instead of writing all code in one file, we break it into different files
# we use modules to better organize our code, instead of writing all code in one file we break it into
# different files. each file is called a module. Each module should contain all related functions and classes
# Then we can import one module into another module
# here we are importing COnvertors module into Modules.py file
# Two ways to import module , either all functions and classes or specific functions and classes
# just like sections in a super market , like fruits vegetables, cleaning products etc.
# each section can be written in different file
# break code into different modules, break up each code into different files, each file is a module
# its better organized and structured and also we can reuse code

"""
import Convertors # all methods will be imported

print(Convertors.kg_to_lbs(60)) # here we have to prefix the object name before the function call
print(Convertors.lbs_to_kg(150))

"""


from Convertors import kg_to_lbs

print(kg_to_lbs(56)) # no need to add class name