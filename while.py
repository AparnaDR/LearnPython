"""
# guess the secret number using while
secret_no = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    # print(f"Guess {guess_count} : ")
    guess = int(input(f"Guess {guess_count} : "))
    guess_count = guess_count + 1
    if guess == secret_no:
        print("You guessed right")
        break
else:  # else for while loop
    print("You failed")


# print 1 to 5 numbers using while loop

i = 1
while i <= 5:
    print(i)
    i += 1


# do while - there is no do while in python, but we can replicate it
# print 5 at-least once before condition fails

i = 5
while True:
    print(i)
    if i >= 5:
        break



# keep asking for user to enter a name if the entered name is invalid
# check for length of the name and is printable, is only aplha

min_length = 2
name = input("Enter your name: ")

while not(len(name) >= min_length and name.isalpha() and name.isprintable()):
    name = input("Enter your name: ")

print(f"howdy {name}!!")


# in above code we are repeating same lines of code twice, asking user to input the name

min_length = 2
while True:
    name = input("Enter your name: ")
    if len(name) >= min_length and name.isalpha() and name.isprintable():
        print(f"howdy {name}!!")
        break


# continue
# program to print odd numbers

i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)




# while - else
# find a value in a list if its not there append that value to the list

li = [1, 2, 3, 10]
val = 10
found = False
i = 0
while i < len(li):
    if li[i] == val:
        found = True
        break
    i += 1
else:
    li.append(val)
print(li)



# while inside try..except..finally
# catch zeroexceptionerror

a = 10
b = 0  # change this to 1 and also check the output

try:
    a/b
except ZeroDivisionError:
    print('divided by zero')
finally:
    print('will always execute')


"""
# increment a and decrement b and catch the eexception when it reaches 0 and make sure the loop doesnt break when an
# exception occurs
# try replacing continue with break

a = 0
b = 2

while a < 4:
    print('-------------------------')
    a += 1
    b -= 1

    try:
        a/b

    except ZeroDivisionError:
        print(f"{a} , {b} -- division by 0")
        continue # if we dont put continue it will go ahead with the next line of code, but finally will still
        # execute if continue is there
    finally:
        print(f"{a} , {b} ---- always executes")

    print("{0},  {1} -- main loop".format(a,b))
else:
    print ("code executed without div error")  # to get this in output tweak b to higher number






