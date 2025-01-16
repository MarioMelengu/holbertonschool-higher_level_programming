#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    arguments = len(argv) - 1
    if arguments > 1:
        print("{} arguments:".format(arguments))
    elif arguments == 1:
        print("{} argument:".format(arguments))
    else:
        print("{} arguments:".format(arguments))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
