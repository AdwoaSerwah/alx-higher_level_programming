#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv) - 1
    if argv_len > 1:
        arg = "arguments:"
    elif argv_len == 1:
        arg = "argument:"
    else:
        arg = "arguments."
    print("{} {}".format(argv_len, arg))
    for i in range(1, argv_len + 1):
        print("{}: {}".format(i, argv[i]))
