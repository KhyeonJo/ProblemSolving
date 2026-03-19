from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [0]*(N+1)
G = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
    
for i in range(1, N+1):
    G[i].sort()

q = deque([R])
cnt = 1

while q:
    node = q.popleft()
    if visited[node]==0:
        visited[node] = cnt
        cnt +=1
        
        for i in G[node]:
            q.append(i)

for i in visited[1:]:
    print(i)