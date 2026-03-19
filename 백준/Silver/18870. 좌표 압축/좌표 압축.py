import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

st = set(L)
srtL = sorted(list(st))

dict = {}

for i in range(len(srtL)):
    dict[srtL[i]] = i #i가 등수

for i in range(N):
    print(dict[L[i]], end = ' ')