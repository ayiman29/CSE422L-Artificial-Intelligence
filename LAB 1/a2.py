from collections import defaultdict
import heapq


n, m = map(int, input().split())
start, goal = map(int, input().split())
heuristic = {}

for _ in range(n):
    v, h = map(int, input().split())
    heuristic[v] = h

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  
'''

n, m = 5, 5
start, goal = 2, 4
heuristic = {
    1: 0,
    2: 2,
    3: 2,
    4: 0,
    5: 1
}
graph = {
    1: [4],
    2: [4, 3, 5],
    3: [2, 5],
    4: [1, 5, 2],
    5: [2, 4, 3]
}

'''
def dijkstra(graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        curr_dist, u = heapq.heappop(heap)

        if curr_dist > dist[u]:
            continue

        for v in graph[u]:
            new_dist = curr_dist + 1
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist

distance = dijkstra(graph, goal)

def admissible(heuristics, distance):
    for i in range(1, n+1):
        if heuristics[i] > distance[i]:
            return 0
    return 1


print(admissible(heuristic, distance))