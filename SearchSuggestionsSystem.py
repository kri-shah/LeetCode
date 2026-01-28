class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def lower_bound(prefix, l, r):
            while l < r:
                m = (l + r) // 2
                if products[m] < prefix:
                    l = m + 1
                else:
                    r = m
                
            return l
        
        res = []
        
        left = 0
        right = len(products)
        prefix = ""
        
        for i in range(len(searchWord)):
            prefix += searchWord[i]
            l = lower_bound(prefix, left, right)
            r = lower_bound(prefix + '{', l, right)

            bound = min(3, r - l) 
            res.append(products[l : l + bound]) 
            left = l
            right = r

        return res
