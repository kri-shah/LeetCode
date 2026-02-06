class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = {}
        def dp(i, width, max_height):
            key = (i, width, max_height)
            if key in memo:
                return memo[key]
            if i == len(books):
                return max_height
            
            best = max_height + dp(i + 1, books[i][0], books[i][1])

            if width + books[i][0] <= shelfWidth:
                best = min(
                    best,
                    dp(
                        i + 1,
                        width + books[i][0],
                        max(max_height, books[i][1])
                    )
                )
            memo[key] = best
            return memo[key]
        
        return dp(0, 0, 0)
