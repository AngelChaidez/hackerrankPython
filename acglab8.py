#!/usr/bin/env python3.11


import sys
import os
import re
import argparse




testString = "This is a test string!"  
print(testString)

# print first character
print("first character: ", testString[0])

#print last character
print("last character: ", testString[len(testString)-1])

# print length of string
print("length of string: ", len(testString))

# print middle character
print("middle character ", testString[len(testString)//2])

# print reverse character
print("reverse character ", testString[::-1])

# print even index 
print("even index: ", testString[::2])

# print odd index
print("odd index: ", testString[1::2])