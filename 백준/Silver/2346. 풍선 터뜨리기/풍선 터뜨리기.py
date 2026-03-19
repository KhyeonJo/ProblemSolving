import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque(enumerate(map(int, input().split())))

for i in range(N):
    idx, now = dq.popleft()
    print(idx+1, end = ' ')
    if now>0:
        dq.rotate(-now+1)
    else:
        dq.rotate(-now)