class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            graph[account[1]]
            email_to_name[account[1]] = name
            for i in range(2, len(account)):
                graph[account[1]].add(account[i])
                graph[account[i]].add(account[1])
                email_to_name[account[i]] = name
        
        visited = set()
        
        def dfs(node):
            path.append(node)
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        res = []
        for account in accounts:
            for i in range(1, len(account)):
                if account[i] not in visited:
                    path = []
                    dfs(account[i])
                    res.append(sorted(path))
        
        for emails in res:
            emails.insert(0, email_to_name[emails[0]])
        return res
