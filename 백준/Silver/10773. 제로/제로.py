import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    now =int(sys.stdin.readline())
    if now ==0:
        dq.pop()
    else:
        dq.append(now)

print(sum(dq))