# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
        traverse into a list to get  [1,2,3,null,null,4,5]
        we inerate through the list, cast, and append to serialize_tree string variable
        how to handle null? if null, we append "#"     
        '''
        result = []
        def traverse(root):
            if not root:
                result.append('#')
                return
            result.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        pointer = [0]
        
        def traverse(p):
            if res[p[0]] == "#":
                p[0] += 1
                return None
            root = TreeNode(int(res[p[0]]))
            p[0] += 1
            root.left = traverse(p)
            root.right = traverse(p)
            return root
        return traverse(pointer)

