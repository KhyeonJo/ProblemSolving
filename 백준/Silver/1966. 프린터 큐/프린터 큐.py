import sys
from collections import deque

times = int(sys.stdin.readline().strip())

for i in range(times):
    st = 0
    N, M = map(int, sys.stdin.readline().split())
    dq = deque(map(int, sys.stdin.readline().split()))
    
    while dq:
        front = dq[0]
        if front < max(dq):
            dq.append(dq.popleft())
        else :
            st += 1
            if M == 0:
                break
            dq.popleft()
        if M == 0:
            M = len(dq)
        M -=1

    print(st)