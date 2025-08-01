import sys

input_year = int(sys.stdin.readline())

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(1)
else:
    print(0)