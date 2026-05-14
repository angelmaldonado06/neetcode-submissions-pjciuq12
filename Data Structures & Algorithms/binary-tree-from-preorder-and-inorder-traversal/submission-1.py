# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
preorder: start at root, goes left and then right
inorder: starts from left node, ends at the right

preorder = [1,2,3,4], inorder = [2,1,3,4]

first index of preorder is 1 => this is the root
find index of element 1 in inorder array to identify the middle or root
the left side of the element 1 in inorder array is the left subtree, the right side is the right subtree


'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])

        return root

'''
Recursive Trace
buildTree([1,2,3,4], [2,1,3,4])
    root = 1, m = 1
    root.left = buildTree([2], [2])
        root = 2, m = 0
        root.left = buildTree([], [])
            return None
        root.right = buildTree([2], [])
            return None
        return Node(2)
    root.right = buildTree([3,4], [3,4])
        root = 3, m = 0
        root.left = buildTree([], [])
            return None
        root.right = buildTree([4], [4])
            root = 4, m = 0
            root.left = buildTree([], [])
                return None
            root.right = buildTree([], [])
                return None
        return Node(4)
    return Node(3, right=Node(4))
return Node(1, left=Node(2), right=Node(3, right=Node(4)))


'''
        
