def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d} ".format(matrix[i][j]),end="")
        print("")
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
