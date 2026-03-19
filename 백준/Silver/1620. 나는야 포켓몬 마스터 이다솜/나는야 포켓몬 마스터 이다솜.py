import sys

N, M = map(int, sys.stdin.readline().split())

index_to_name = {}
name_to_index = {}

for i in range(N):
    now = sys.stdin.readline().strip()
    index_to_name[i+1] = now
    name_to_index[now] = i+1

for i in range(M):
    now = sys.stdin.readline().strip()
    if now.isdigit():
        print(index_to_name[int(now)])
    else:
        print(name_to_index[now])