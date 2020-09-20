import sys
import math

n = int(input())
pi = []

for i in range(n):
    pi.append(int(input()))

pi = sorted(pi)
lowest = pi[-1]

for i in range(n - 1):
    lowest = min(abs(pi[i] - pi[i + 1]), lowest)

print(lowest)
