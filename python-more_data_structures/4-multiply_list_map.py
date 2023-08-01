def square_matrix_map(matrix=[]):
    my_list = [1, 2, 3, 4, 6]
    return(list(map(lambda row: list(map(lambda x: x*x, row)), matrix)))