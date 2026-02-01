class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build graph:
        graph = {}   # the graph is saved like this: node.val:[neighbors], where neighbors is a list of lists [neighbor.val, edge_value]
        graph = {}
        for i, (v1, v2) in enumerate(equations):
            div = values[i]
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []
            graph[v1].append([v2, div])
            graph[v2].append([v1, 1/div])
        
        
        # 2. compute_path function, to get the total value along the graph
        def compute_path(a,b):
            visited = set()
            path = []
            q = deque()
            q.append([a, 1])

            while q:
                curr_node, curr_val = q.popleft()
                if curr_node in visited:
                    continue
                visited.add(curr_node)
                neighbors = graph[curr_node]
                for x, val in neighbors:
                    if x == b:
                        return curr_val * val
                    else:
                        q.append([x, curr_val * val])
        
            return -1


        # 3. prepare the result 
        res = []
        for v1, v2 in queries:
            if v1 not in graph or v2 not in graph:
                res.append(-1)
            elif v1 == v2:
                res.append(1)
            else:
                res.append( compute_path(v1, v2) )   # path = [2, 4, 5] (edge values) or path = -1 (no path )


        return res
