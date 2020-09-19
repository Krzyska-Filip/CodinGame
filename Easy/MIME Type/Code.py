import sys
import math

n, q = int(input()), int(input())
arrExt = {}

for i in range(n):
    ext, mime = input().split()
    arrExt[ext.lower()] = mime
for i in range(q):
    fname = input().lower()
    dotIndex = fname.rfind('.')
    if dotIndex != -1 or dotIndex == len(fname):
        fname = fname[dotIndex + 1:]
        print(arrExt.get(fname, "UNKNOWN"))
    else:
        print("UNKNOWN")
