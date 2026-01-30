class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(lambda: defaultdict(int))
        n = len(source)
        dp = [inf] * (n+1)
        dp[n] = 0
        change_lengths = sorted(set(len(sub) for sub in original))
        originalSet, changedSet = set(original),  set(changed)
        cache = defaultdict(tuple)

        for i, s in enumerate(original):
            t, c = changed[i], cost[i]
            adj[s][t] = min(adj[s][t], c) if t in adj[s] else c

        def dijkstra(s, t):
            heap = [(0, s)]
            costs = defaultdict(lambda: inf)
            costs[start] = 0
            while heap:
                c, v = heapq.heappop(heap)
                if v == t:
                    return c
                for u in adj[v]:
                    newCost = adj[v][u] + c
                    if newCost < costs[u]:
                        costs[u] = newCost
                        heapq.heappush(heap, (costs[u], u))
            return inf

        for i in range(n-1, -1, -1):
            if target[i] == source[i]:
                dp[i] = dp[i+1]
            for length in change_lengths:
                start, end = i, i+length
                if end > n:
                    break
                s = source[start:end]
                t = target[start:end]
                if s in originalSet and t in changedSet:
                    key = (s, t)
                    cache[key] = cache[key] if key in cache else dijkstra(s, t)
                    dp[i] = min(dp[i], cache[key] + dp[end])

        return dp[0] if dp[0] != inf else -1