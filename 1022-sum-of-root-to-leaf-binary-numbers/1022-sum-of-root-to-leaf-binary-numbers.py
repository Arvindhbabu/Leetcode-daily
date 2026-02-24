# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, str(root.val))])
        summ = 0
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                val = '0b' + val
                summ += int(val, 2)
            
            if node.left:
                queue.append((node.left, val + str(node.left.val)))
            if node.right:
                queue.append((node.right, val + str(node.right.val)))
        return summ 