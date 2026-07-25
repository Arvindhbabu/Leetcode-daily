# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(temp, depth):
            if not temp:
                return
            if depth == len(arr):
                arr.insert(0, [])
            arr[len(arr) - depth - 1].append(temp.val)
            traverse(temp.left, depth + 1)
            traverse(temp.right, depth + 1)
        
        arr = []
        traverse(root, 0)
        return arr
            