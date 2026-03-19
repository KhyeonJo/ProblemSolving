import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
chk_list = list(map(int, input().split()))
start_deque = list(map(int, input().split()))
M = int(input())
insert_list = list(map(int, input().split()))

dq = deque()

for i in range(N):
    if chk_list[i]==0:
        dq.append(start_deque[i])

for i in range(M):
    dq.appendleft(insert_list[i])
    print(dq.pop(), end = ' ')