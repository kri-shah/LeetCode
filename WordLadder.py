class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        
        visited = set()

        while queue:
            word, path = queue.popleft()
            if word == endWord:
                return path 
            for i in range(len(word)):
                temp = [x for x in word]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    temp[i] = c
                    new = "".join(temp)
                    if new in word_set and new not in visited:
                        visited.add(new)
                        queue.append((new, path + 1))

        return 0
