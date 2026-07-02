""" Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
Example 1
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation:
Element position (1,1) is 0, so set entire row 1 and column 1 to 0. """
def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Find rows and columns containing zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set rows to zero
    for i in zero_rows:
        for j in range(cols):
            matrix[i][j] = 0

    # Set columns to zero
    for j in zero_cols:
        for i in range(rows):
            matrix[i][j] = 0


# -------- Main Program --------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("\nEnter matrix elements row-wise:")

for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))

    while len(row) != cols:
        print(f"Please enter exactly {cols} elements.")
        row = list(map(int, input(f"Row {i+1}: ").split()))

    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Apply Set Matrix Zeroes
set_zeroes(matrix)

print("\nMatrix after applying Set Matrix Zeroes:")
for row in matrix:
    print(row)