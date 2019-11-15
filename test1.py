# print("aparna")
# print("     *")
# print("    *" * 2)
# print("   *" * 3)
# print("  *" * 4)
# print(" *" * 5)
#
# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")
# print(name+" likes " + color)

#
# weight_in_pounds = input("Enter your weight in pounds" )
# weight_in_kgs = int(weight_in_pounds) * 0.453592
# print(weight_in_kgs)
####################
# house_price = 1000000
# has_good_credit = False
# downPayment = 0
#
# if has_good_credit:
#     downPayment = house_price * (10/100)
# else:
#     downPayment = 0.2 * house_price
#
#
#print(f"DownPayment amount is ${downPayment}")


name = 'aparna'
if len(name) < 3:
    print("name must be atleast 3 characters long")
elif len(name) > 50:
    print("name can be a maximum of 50 characters only")
else:
    print("name looks good!!")
