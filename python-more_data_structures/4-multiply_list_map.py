#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return(list(map(lambda row: list(map(lambda x: x*x, row)), matrix)))