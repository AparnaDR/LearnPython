# key value pairs
# cannot contain duplicate keys

"""
customer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verified" :  True,
    "age" : 30 # warning -  age is duplicated
}

print(customer)

# change value of an key
customer["name"] = "mike smith"
print(customer)

# both gives same result when valid data is fetched or key is fetched
print(customer.get("name"))
print(customer["age"])

# when invalid data is fetched
print(customer.get("dob")) # None is returned on the console
# print(customer["dob"]) # error is displayed on the console

# assign default value when key not found, can be dne while using an get
# Instead on None we ger default value
print(customer.get("dob","Jan 1 2001"))
"""
# exercise
numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

digits = input("number: ")

output  = ""
for ch in digits:
    #output += (numbers[ch]) + " "
    output += (numbers.get(ch , '!') + " ")
print (output)

