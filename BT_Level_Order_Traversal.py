# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        queue = []
        queue.append(root)
        
        output = []
        output.append([root.val])

        while queue:
            tout = []
            tqueue = []
            for node in queue:
                if node.left:
                    tout.append(node.left.val)
                    tqueue.append(node.left)
                if node.right:
                    tout.append(node.right.val)
                    tqueue.append(node.right)
            queue = tqueue
            if tout:
                output.append(tout)

        return output
