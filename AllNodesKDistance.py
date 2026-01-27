# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph():
            queue = deque()
            queue.append(root)

            while queue:
                q_len = len(queue)
                for _ in range(q_len):
                    node = queue.popleft()
                    if node.left:
                        graph[node.val].append(node.left.val)
                        graph[node.left.val].append(node.val)
                        queue.append(node.left)
                    if node.right:
                        graph[node.val].append(node.right.val)
                        graph[node.right.val].append(node.val)
                        queue.append(node.right)
        
        build_graph()
        res = []
        queue = deque()
        for val in graph[target.val]:
            queue.append((val, target.val))

        dist = 0
        while queue:
            dist += 1
            
            if dist == k:
                res = [i for i, y in queue]
                return res
            
            q_len = len(queue)
            for _ in range(q_len):
                node, prev = queue.popleft()
                for neigh in graph[node]:
                    if neigh == prev:
                        continue
                    
                    queue.append((neigh, node))
        
        return [target.val] if k == 0 else []
        
