class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_map = {")":"(", "]" : "[", "}" : "{"}
        for ch in s:
            if ch in h_map.values():
                stack.append(ch)
            elif ch in h_map.keys():
                if not stack or stack.pop() != h_map[ch]:
                    return False
        return not stack