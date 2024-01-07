#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxim = my_list[0]
        for i in my_list:
            if maxim < i:
                maxim = i
        return maxim
