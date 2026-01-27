class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w * 2)) 

        minHeap = [(0, 0)]  # (cost, node)
        dist = [float('inf')] * n
        dist[0] = 0

        while minHeap:
            cost, u = heapq.heappop(minHeap)

            if u == n - 1:
                return cost
            # if cost > dist[u]:
            #     continue
            for v, w in adj[u]:
                newCost = cost + w
                if newCost < dist[v]:
                    dist[v] = newCost
                    heapq.heappush(minHeap, (newCost, v))

        return -1