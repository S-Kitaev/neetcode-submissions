# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if root is None:
            return []
        v = root
        parents = [v]

        result.append([v.val])

        while parents:
            children = []
            ch_result = []
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                    ch_result.append(parent.left.val)
                if parent.right:
                    children.append(parent.right)
                    ch_result.append(parent.right.val)

            result.append(ch_result)
            parents = children

        return result[:-1]
        