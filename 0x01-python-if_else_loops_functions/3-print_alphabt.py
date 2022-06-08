#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if char(a) is not 'q' and char(a) is not 'e':
        print("{:s}".format(char(a)), end="")
