class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def find_start():
            for row, arr in enumerate(mat):
                for col, i in enumerate(arr):
                    if i == 0:
                        start = [row, col]
                        return start
        start = find_start()
        queue = [start]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        res = [[float('inf')] * len(mat[0])] * len(mat) 
        visited = set()
        while queue:
            coords = queue.pop()
            
            for d in directions:
                if coords[0] + d[0] > 0 and coords[1] + d[1] > 0 and coords[0] + d[0] < len(mat) and coords[1] + d[1] < len(mat[0]):
                    if mat[coords[0] + d[0]][coords[1] + d[1]] == 0:
                        res[coords[0] + d[0]][coords[1] + d[1]] = 0
                    else:
                        res[coords[0] + d[0]][coords[1] + d[1]] = min(res[coords[0] + d[0]][coords[1] + d[1]], mat[coords[0]][coords[1]] +1)
                    if tuple([coords[0]+d[0], coords[1]+d[1]]) not in visited:
                        queue.append([coords[0]+d[0], coords[1]+d[1]])
                        visited.add(tuple([coords[0]+d[0], coords[1]+d[1]]))
        return res
