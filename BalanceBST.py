# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            arr.append(node.val)
            in_order(node.right)
        
        def construct(s, e):
            if s > e:
                return
            
            m = (s + e) // 2
            node = TreeNode(arr[m])
            left = construct(s, m - 1)
            right = construct(m + 1, e)
            node.left = left
            node.right = right
            
            return node
        
        in_order(root)
        new_root = construct(0, len(arr) - 1)
        
        return new_root
        
