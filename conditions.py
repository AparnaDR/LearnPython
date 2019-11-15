weight = input("Weight: ")
# weight = int(input("Weight: ")
weight_type = input("(L)bs or (K)gs: ")

# converting lbs to kgs
if weight_type == 'L' or weight_type == 'l':
    weight_in_kgs = int(weight) * 0.457
    print(f"You are {weight_in_kgs} kilos")
elif weight_type.upper() == 'K':
    weight_in_lbs = int(weight) / 0.45
    print(f"You are {weight_in_lbs} pounds")
else:
    print("invalid weight type!!")

# not useful for blocks of codes
a =25
b = 'a less than 25' if a < 5 else 'a >= 5'
print(b)
