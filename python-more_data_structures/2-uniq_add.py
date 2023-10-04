#!/usr/bin/python3
def uniq_add(my_list=[]):
    empty_list = []
    element = 0
    total = 0
    for number in my_list:
        if number not in empty_list:
            empty_list.append(number)
    while element < len(empty_list):
        total = total + empty_list[element]
        element += 1
    return total
