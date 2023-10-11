'''
This file may prove useful for adding utility functions to write further code (mostly esolangs).
Other files may work, but Python may prove to be the most intuitive in this case.

When adding a utility function, add a comment to describe what it does and what it is for.
'''

import math


def str2bf(obj):  # Takes string (or iterable) 'obj' and returns the code for how to output 'obj' in esolang BF as a string.
    prev = 0
    n = str()
    for curr in map(ord, obj):
        if curr != prev:
            if curr > prev:
                n += '+' * (curr - prev)
            else:
                n += '-' * (prev - curr)
        prev = curr
        n += '.'
    return n



def linear_combo(n):  # Relatively optimal means of getting a linear combo + optional i for squares.
    s = round(math.sqrt(n)) + 1  # Add one to count for squares
    ret_val = (0, 0, n)
    prev = n  # Worst case scenario for length representation

    while n % s != 0 or s > 1:  # Case 1: Lower or equal
        s -= 1
        a = (n // s)
        b = n - (s * a)
        curr = s + a + b
        if curr < prev:
            ret_val = (s, a, b)
            prev = curr
    return ret_val


def str2bf2(obj):  # A more optimized implementation, using more advanced principles to save space / memory
    n = str()
    char = ''
    prev = 0

    for curr in map(ord, obj):
        if curr > prev:
            char = '+'
        else:
            char = '-'

        first = ""
        middle = ""
        last = ""

        l_c = linear_combo(abs(curr - prev))

        if l_c[0] > 0:  # Due to how linear_combo works, l_c[1] has a value if l_c[0] does
            first = '+' * l_c[0]
            middle = f"[<{char * l_c[1]}>-]"

        last = char * l_c[2]

        n += f">{first}{middle}<{last}."
        prev = curr
    return n


def message():
  print("John Cyberclub")


if __name__ == "__main__":
  message()
