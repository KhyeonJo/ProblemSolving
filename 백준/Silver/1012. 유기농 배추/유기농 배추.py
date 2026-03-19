import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y): #좌표(x, y) -> 이 좌표가 1이면 -> -1로 바꾸고 상하좌우 검색(dfs재귀보냄. 각 방향에 1개씩 4방향)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    cnt = 0
    for a in range(M):
        for b in range(N):
            if graph[b][a] == 1:
                dfs(a, b)
                cnt +=1
    print(cnt)