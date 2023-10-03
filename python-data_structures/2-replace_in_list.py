#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenght = len(my_list)
    if idx < 0 or idx > lenght - 1:
        return my_list

    my_list[idx] = element
    return my_list
