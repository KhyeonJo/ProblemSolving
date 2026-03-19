import sys
from collections import Counter

L = Counter(sys.stdin.readline().strip().upper())
if len(L)==1:
    print(L.most_common()[0][0])
elif L.most_common()[0][1]==L.most_common()[1][1]:
    print('?')
else:
    print(L.most_common()[0][0])