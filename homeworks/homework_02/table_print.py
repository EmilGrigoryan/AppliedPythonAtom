import json
import csv


def print_tab(data):
    max_lengths = []
    for i in range(len(data[0]) - 1):
        comparing = []
        for j in range(1, len(data)):
            comparing.append(data[j][i])
        max_lengths.append(len(max(comparing,
                                   key=lambda el: 1 if type(el) == int
                                   else len(el))))
    lenght = len(data[0])
    max_lengths.append(len(data[0][lenght - 1]))
    Sum = 0
    for i in max_lengths:
        Sum += i
    print('-' * (sum(max_lengths) - 3) + '-' * (len(max_lengths) * 6))
    print('|', end='')
    for k in range(len(data[0])):
        d = max_lengths[k]
        u = len(str(data[0][k]))
        t = (d - u) // 2
        print(' ' * (t + 1), data[0][k],
              ' ' * (d - (t + u)), '|', end='')
    print()
    for i in range(1, len(data)):
        print('|', end='')
        for j in range(len(data[i])):
            if j == len(data[i]) - 1:
                d = max_lengths[k]
                u = len(str(data[j][k]))
                print(" " * (d - u + 1), data[i][j], " |", end='')
            else:
                print(" ", data[i][j],
                      ' ' * (max_lengths[j] - len(str(data[i][j]))),
                      '|', end='')
        print()
    print('-' * (sum(max_lengths) - 3) + '-' * len(max_lengths) * 6)
    return
