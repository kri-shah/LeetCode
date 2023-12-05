#Beats 64.65%of users with Python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recurse(self, r1, r2):
            if r1 is None and r2 is None:
                return 1
            elif r2 is None:
                return 0
            elif r1 is None:
                return 0
            
            if r1.val != r2.val:
                return 0
            
            
            left = self.recurse(r1.left, r2.left)
            right = self.recurse(r1.right, r2.right)
            return(min(left, right)) 
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        

        
        return self.recurse(p, q)
