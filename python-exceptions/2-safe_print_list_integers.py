#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    el_inlist = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                el_inlist += 1
            else:
                continue
        except IndexError:
            raise IndexError
            break
    print()
    return el_inlist
