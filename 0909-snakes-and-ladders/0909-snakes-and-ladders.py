from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        
        def get_pos(num):
            r, c = divmod(num - 1, n)
            if r % 2 == 0:
                return (n - 1 - r, c)
            return (n - 1 - r, n - 1 - c)

        visited = [False] * (n * n + 1)
        q = deque([1])
        visited[1] = True
        moves = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == n * n:
                    return moves
                for i in range(1, 7):
                    nxt = curr + i
                    if nxt > n * n:
                        continue
                    r, c = get_pos(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            moves += 1

        return -1