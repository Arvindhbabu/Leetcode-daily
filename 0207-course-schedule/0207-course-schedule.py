class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i: [] for i in range(numCourses)}
        in_degrees = [0] * numCourses

        # set up In Degrees for topological sort
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        out = 0
        q = deque([x for x in range(numCourses) if in_degrees[x] == 0])

        while q:
            u = q.popleft()
            for v in adj[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    q.append(v)
            out += 1
        
        return out == numCourses

        