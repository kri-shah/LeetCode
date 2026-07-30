class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1

        frequencies = [fr for _, fr in freq.items()]
        frequencies.sort(reverse=True)
        
        res = 0
        count = 0
        for i, freq in enumerate(frequencies):
            if i % 8 == 0:
                count += 1
            res += freq * count
        
        return res
