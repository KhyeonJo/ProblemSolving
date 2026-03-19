import heapq
INF = float('inf')

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dksta(start_node):
    path_values = [INF] * (N+1)
    path_values[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))
    
    while queue:
        weight, start = heapq.heappop(queue)
        if weight > path_values[start]:
            continue
    
        for next_vortex, add_weight in graph[start]:
            true_weight = weight + add_weight
            if true_weight < path_values[next_vortex]:
                path_values[next_vortex] = true_weight
                heapq.heappush(queue, (true_weight, next_vortex))
    return path_values

one_to_u = dksta(1)[u]
u_to_v = dksta(u)[v]
v_to_N = dksta(v)[N]
tot1 = one_to_u + u_to_v + v_to_N

one_to_v = dksta(1)[v]
v_to_u = dksta(v)[u]
u_to_N = dksta(u)[N]
tot2 = one_to_v + v_to_u + u_to_N

if min(tot1, tot2) == INF:
    print(-1)
else:
    print(min(tot1, tot2))