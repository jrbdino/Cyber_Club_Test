'''
This file may prove useful for adding utility functions to write further code (mostly esolangs).
Other files may work, but Python may prove to be the most intuitive in this case.

When adding a utility function, add a comment to describe what it does and what it is for.
'''


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


def message():
  print("John Cyberclub")


if __name__ == "__main__":
  message()
