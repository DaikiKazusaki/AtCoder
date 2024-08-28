# 最短経路問題 -> ダイクストラ法
# ダイクストラ法: ある頂点から他の全ての頂点への最短経路を求めるアルゴリズム
# dict = start からの最短距離のリスト，正の無限大(=float('inf'))で初期化
# q = (0, start) というタプルを要素とするリスト

import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, u = heapq.heappop(q)
        if dist[u] < cost:
            continue
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heapq.heappush(q, (dist[v], v))
    return dist

# 重み付き隣接リストの作成
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, x = map(int, input().split())
    graph[i].append([i + 1, a])
    graph[i].append([x - 1, b])
x = dijkstra(graph, 0)
print(x.pop(len(x) - 1))
