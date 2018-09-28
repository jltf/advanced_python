"""
Homework 2.

Write a script which causes segmentation fault at Python 3 interpreter.
"""

import ctypes

print(ctypes.c_char.from_address(1))
