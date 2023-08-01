def square_matrix_simple(matrix=[]):
    new_matrix=[]
    for i in matrix:
        item=list(map(lambda x,y:x*y,i,i))
        new_matrix.append(item)
    return new_matrix
