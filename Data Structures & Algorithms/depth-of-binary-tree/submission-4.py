# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        d = root
        parents = [d]
        depth = 1
        while parents:
            children = []
            for parent in parents:
                if parent.left:
                    children += [parent.left]
                if parent.right:
                    children += [parent.right]

            if len(children) != 0:
                depth += 1
            parents = children

        return depth
        