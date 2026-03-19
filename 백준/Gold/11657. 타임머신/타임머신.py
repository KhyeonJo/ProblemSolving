import sys

input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
edges = [] #그래프
dist = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

def bellman_ford(start):
    dist[start] = 0 #시작 노드 초기화
    
    # n번의 라운드 반복
    for i in range(n):
        # 매 반복마다 모든 간선을 확인
        for u, v, w in edges:
            # 1. 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # 2. 단, 시작점(1번 노드)에서 도달 가능한 노드(dist[u] != INF)여야 함
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                
                # n번째 라운드에서도 값이 갱신된다면 '음의 사이클' 존재
                if i == n - 1:
                    return True
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    # 음의 사이클이 발생
    print("-1")
else:
    # 1번 노드를 제외한 다른 노드로 가는 최단 거리 출력
    for i in range(2, n + 1):
        if dist[i] == INF:
            # 도달할 수 없는 경우
            print("-1")
        else:
            print(dist[i])