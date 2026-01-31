class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        
        while l < r:
            m = (l + r) // 2
            if target < letters[m]:
                r = m
            else:
                l = m + 1
        
        return letters[l] if letters[l] > target else letters[0]
