from collections import Counter
import sys
N, M = map(int, sys.stdin.readline().split())

L = []

for i in range(N):
    L.append(sys.stdin.readline().strip())

L_new = []

for _ in L:
    if len(_)>=M:
        L_new.append(_)
      
counter_dic = Counter(L_new)

st = set(L_new)
L_new = list(st)

L_new.sort()
L_new.sort(key=lambda x: (counter_dic[x],len(x)), reverse=True)

for i in range(len(L_new)):
    print(L_new[i])