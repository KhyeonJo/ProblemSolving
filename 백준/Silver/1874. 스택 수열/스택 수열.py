import sys
from collections import deque

N = int(sys.stdin.readline().strip())
given = deque()

for i in range(N):
    given.append(int(sys.stdin.readline().strip()))

dq = deque(range(1, N+1))
keep = []
answer = []
while len(answer)<(2*N):
    if len(keep) == 0 or keep[-1]!=given[0]:
        if len(dq)==0:
            break
        keep.append(dq.popleft())
        answer.append('+')
    elif keep[-1]==given[0]:
        keep.pop()
        given.popleft()
        answer.append('-')
if len(given)==0:
    for i in range(len(answer)):
        print(answer[i])
else :
    print("NO")