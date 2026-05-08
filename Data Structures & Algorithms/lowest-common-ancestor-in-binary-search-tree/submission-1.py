# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        base case: if root is none, or root is p, or root is q: return root
        recurse left, recurse right
        if both sides returned something -> corrent node is LCA: return root
        if only one side returned something -> return that side       
        
        '''

        if root is None or root.val == p.val or root.val == q.val:
                return root

        side1 = self.lowestCommonAncestor(root.left, p, q)
        side2 = self.lowestCommonAncestor(root.right, p, q)

        if side1 and side2:
            return root
        return side1 if side1 else side2        