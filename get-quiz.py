#!/usr/bin/env python3

# l from https://engineering-application.britecore.com/us/devops-director
l = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98,
      114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 119, 115, 109, 118, 106, 101, 102, 110, 118, 119, 109, 100, 107, 118, 110, 101, 110 ]

# I suspected l was a list of ascii, but didn't know it. Never got the list comprehension suggestion, but probably something to do list ''.join(i) to get a single string at the end.
for i in l: print(chr(i), end='')
print()