import sys

N, K = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))

sumL = [0]
j = 0

for i in L:
    sumL.append(i+j)
    j=i+j

results = []

for i in range(N-K+1):
    results.append(sumL[i+K]-sumL[i])



print(max(results))