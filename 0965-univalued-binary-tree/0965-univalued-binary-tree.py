# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        target = root.val
        quene = deque([root])
        visited = set()
        
        while quene:
            node = quene.popleft()

            if node:
                visited.add(node.val)
                quene.append(node.left)
                quene.append(node.right)
        
        return len(visited) == 1