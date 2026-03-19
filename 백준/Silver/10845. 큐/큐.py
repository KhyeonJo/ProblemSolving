import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    now = sys.stdin.readline().strip()
    if now[1]=='u':
        A, B = now.split()
        dq.append(B)
    elif now =='pop':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif now =='size':
        print(len(dq))
    elif now =='empty':
        print(int(len(dq)==0))
    elif now =='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])