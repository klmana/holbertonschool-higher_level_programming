#!/usr/bin/python3
for number_i in range(10):
    for number_j in range(10):
        if number_i < number_j:
            print('{:d}{:d}'.format(number_i, number_j), end='')
            if number_i < 8:
                print(', ', end='')
    print()
