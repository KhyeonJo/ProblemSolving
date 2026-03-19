from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [0] * (N+1)

G = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

q = deque([1])
cnt = -1

while q:
    node = q.popleft()
    if visited[node]==0:
        visited[node] = 1
        cnt +=1
        
        for i in G[node]:
            q.append(i)

print(cnt)