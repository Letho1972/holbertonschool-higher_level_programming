#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    lenght = len(my_list)
    i = 0

    while i < lenght:
        if new_list[i] == search:
            new_list[i] = replace
        i += 1
    return new_list
