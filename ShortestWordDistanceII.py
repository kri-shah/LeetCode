class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        self.map = defaultdict(list)
        
        for i, word in enumerate(self.words):
            self.map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1 = self.map[word1]
        w2 = self.map[word2]
        p1 = 0
        p2 = 0
        res = float('inf')

        while p1 < len(w1) and p2 < len(w2):
            res = min(abs(w1[p1] - w2[p2]), res)
            if w1[p1] < w2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return res




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
