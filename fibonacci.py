#!/usr/bin/env python3.11


import sys


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    user = input("Enter a number: ")
    print(fibonacci(int(user)))


