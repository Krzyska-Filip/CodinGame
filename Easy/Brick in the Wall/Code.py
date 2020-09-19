import sys
import math

def sumLayer(BricksLeft, L):
    W = ((L - 1) * 6.5 / 100) * 10 * BricksLeft
    return(W)

x, n = int(input()), int(input())
BricksLeft = input().split()
BricksLeft = [int(x) for x in BricksLeft]
BricksLeft = sorted(BricksLeft)
Work = 0
L = 1

while len(BricksLeft) >= 1 :
    TheHeaviestBricks = max(len(BricksLeft) - x, 0)
    BricksInCurrentLayer = BricksLeft[TheHeaviestBricks:]
    BricksLeft = BricksLeft[0:TheHeaviestBricks]
    Work += sumLayer(sum(BricksInCurrentLayer), L)
    L += 1

print(format(Work, '.3f'))
