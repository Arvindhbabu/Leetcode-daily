class node:
    def __init__(self):
        self.childs = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = node()
            curr = curr.childs[char]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(curr, i):
            if i == len(word):
                return curr.end

            char = word[i]

            if char == '.':
                for child in curr.childs.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if char not in curr.childs:
                return False

            return dfs(curr.childs[char], i + 1)

        return dfs(self.root, 0)