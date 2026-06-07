# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_to_node = defaultdict(TreeNode)
        root = set([node for node, _, _ in descriptions])

        for node, child, dirr in descriptions:
                if child in root:
                    root.remove(child)
                
                if node not in val_to_node:
                    val_to_node[node] = TreeNode(node)
                
                if child not in val_to_node:
                    val_to_node[child] = TreeNode(child)
                
                if dirr:
                    val_to_node[node].left = val_to_node[child]
                else:
                    val_to_node[node].right = val_to_node[child]
        
        return val_to_node[root.pop()]
