#!/usr/bin/python3
def no_c(my_string):
    noc_str = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            noc_str += i
    return (noc_str)
