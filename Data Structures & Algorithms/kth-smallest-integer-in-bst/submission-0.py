# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
trasverse the nodes in-order (left -> root -> right) so the values come out in ascending order
while traversing we keep a count variable to track the position of the current node
when count == k, we store it in a global vairable and return that value

'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        result = [None]

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            count[0] += 1
            if count[0] == k:
                result[0] =node.val
            inorder(node.right)

        inorder(root)
        return result[0]

        

        



        