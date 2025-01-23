#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    en_list = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                en_list += 1
            else:
                continue
        except IndexError:
            raise IndexError
            break
    print()
    return en_list
