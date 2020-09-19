import sys
import math

n = int(input())
arr = input().split()
arr = [int(x) for x in arr]
totalCost = 0

while len(arr) > 1:
    arr = sorted(arr)
    arr = arr[::-1]
    arr[-1]   = arr.pop(-1) + arr[-1]
    totalCost += arr[-1]

print(totalCost)
