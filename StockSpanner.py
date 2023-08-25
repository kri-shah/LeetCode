class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1
        if not self.stack:
            self.stack.append((price, 1))
            return 1
    
        while self.stack and self.stack[-1][0] <= price:
            val, span = self.stack.pop()
            ans += span
        self.stack.append((price, ans))
        
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
