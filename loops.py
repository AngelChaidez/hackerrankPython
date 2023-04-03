#!/usr/bin/env python3.11

"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4

"""


if __name__ == '__main__':
    n = int(input())
    m = 0

    while m < n:
        print(m * m)
        m += 1