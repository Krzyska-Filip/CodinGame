import sys
import math

b = input()
arr = b.split('0')
longest = 1

for i in range(len(arr) - 1):
    longest = max(len(arr[i]) + len(arr[i+1]) + 1, longest)

print(longest)
