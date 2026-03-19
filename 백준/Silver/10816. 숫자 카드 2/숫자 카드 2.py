import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
Nlist = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
Mlist = list(map(int, sys.stdin.readline().split()))

cnt_dict = {}

for i in range(N):
    if Nlist[i] in cnt_dict:
        cnt_dict[Nlist[i]] += 1
    else:
        cnt_dict[Nlist[i]] = 1

for i in range(M):
    if Mlist[i] not in cnt_dict:
        print('0', end = " ")        
    else:
        print(cnt_dict[Mlist[i]], end = " ")