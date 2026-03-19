from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

G = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

G_1 = [list[:] for list in G]
G_2 = [list[:] for list in G]

for i in range(1, N+1):
    G_1[i].sort(reverse=True)
    G_2[i].sort()

stack = deque([R])
queue = deque([R])
L_1 = []
L_2 = []
visited_1 = [0] * (N+1)
visited_2 = [0] * (N+1)

while stack:
    node = stack.pop()
    if visited_1[node]==0:
        visited_1[node] = 1
        L_1.append(node)
        for i in G_1[node]:
            stack.append(i)

while queue:
    node = queue.popleft()
    if visited_2[node]==0:
        visited_2[node] = 1
        L_2.append(node)
        for i in G_2[node]:
            queue.append(i)

print(*L_1)
print(*L_2)