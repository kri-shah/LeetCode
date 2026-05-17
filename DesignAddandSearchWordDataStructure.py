class Trie:
    def __init__(self):
        self.children = {}
        self.finished = False
class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.finished = True

    def _search(self, curr, word, i):
        print(i)
        if i == len(word):
            return curr.finished
        if word[i] in curr.children:
            if self._search(curr.children[word[i]], word, i + 1):
                return True
        elif word[i] == '.':
            for child in curr.children.values():
                if self._search(child, word, i + 1):
                    return True
        
        return False

    def search(self, word: str) -> bool:
        return self._search(self.trie, word, 0)
    
       
            



