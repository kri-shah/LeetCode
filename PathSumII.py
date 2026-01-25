# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, cur_sum):
            nonlocal res
            if not node:
                return
            
            cur_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path[:])
                return
                
            dfs(node.left, path, cur_sum)
            dfs(node.right, path, cur_sum)
            path.pop()

        dfs(root, [], 0)
        
        return res
