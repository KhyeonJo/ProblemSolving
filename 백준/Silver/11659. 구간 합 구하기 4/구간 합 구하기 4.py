import sys

N, M = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))
sumL = [0]
j = 0
for i in L:
    sumL.append(i+j)
    j = i+j

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(sumL[end]-sumL[start-1])