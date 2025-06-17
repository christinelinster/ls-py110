# Transpose 3x3 Matrix

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix



matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True