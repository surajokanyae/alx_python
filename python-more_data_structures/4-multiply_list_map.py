def square_matrix_map(matrix=[]):
    x = [1, 2, 3, 4, 5]
    return(list(map(lambda row: list(map(lambda x: x*x, row)), matrix)))