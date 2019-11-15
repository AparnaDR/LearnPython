matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][2]) # first row 2nd element
matrix[0][2] = 22
print(matrix[0][2]) # first row 2nd element modified

# iterate through all elements using nested loop

for row in matrix:
    for item in row:
        print(item)

