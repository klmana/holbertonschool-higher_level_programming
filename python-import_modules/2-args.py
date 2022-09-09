#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentNumbers = len(sys.argv) - 1
    if argumentNumbers is 0:
        print("{:d} arguments.".format(argumentNumbers))
    elif argumentNumbers is 1:
        print("{:d} argument:".format(argumentNumbers))
    else:
        print("{:d} arguments:".format(argumentNumbers))
    for index in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(index, sys.argv[index]))
