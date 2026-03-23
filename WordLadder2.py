class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                w = [c for c in word]
                w[i] = '*'
                graph["".join(w)].append(word)
        
        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            word, cost = queue.popleft()
            if word == endWord:
                return cost
            for i in range(len(word)):
                w = [c for c in word]
                w[i] = '*'
                for neigh in graph["".join(w)]:
                    if neigh in visited:
                        continue
                    queue.append((neigh, cost + 1))
                    visited.add(neigh)
        
        return 0
        
