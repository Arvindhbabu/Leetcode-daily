class Trie():
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.is_end = True

    def prune(self, c):
        child = self.children[c]
        if not child.children and not child.is_end:
            del self.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        prefix = Trie()
        for word in words:
            prefix.add_word(word)

        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []

        def dfs(r, c, node, s):
            s += board[r][c]
            visit.add((r, c))

            child = node.children[board[r][c]]

            if child.is_end:
                res.append(s)
                child.is_end = False

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visit and board[row][col] in child.children:
                    dfs(row, col, child, s)
            visit.remove((r, c))
            node.prune(board[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in prefix.children:
                    dfs(r, c, prefix, "")

        return res