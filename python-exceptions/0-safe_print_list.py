#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    el_inlist = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            el_inlist += 1
        except IndexError:
            break
    print()
    return el_inlist
