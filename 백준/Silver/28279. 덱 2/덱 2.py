from collections import deque
import sys
N = int(sys.stdin.readline())

dq = deque()
L = []

for i in range(N):
    L = sys.stdin.readline().split()
    if L[0] == '1':
        dq.appendleft(L[1])
    elif L[0] == '2':
        dq.append(L[1])
    elif L[0] == '3':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif L[0] == '4':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif L[0] == '5':
        print(len(dq))
    elif L[0] == '6':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif L[0] == '7':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])