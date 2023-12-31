#!/usr/bin/python3


from sys import argv

args_sum = 0

for arg in argv[1:]:
    args_sum += int(arg)


print(args_sum)
