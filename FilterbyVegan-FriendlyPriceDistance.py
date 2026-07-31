class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for rest in restaurants:
            if rest[3] <= maxPrice and rest[4] <= maxDistance:
                if veganFriendly == 1 and rest[2] == 1:
                    res.append(rest)
                elif veganFriendly == 0:
                    res.append(rest)
        res.sort(key=lambda x: (-x[1], -x[0]))
        return [x[0] for x in res]
