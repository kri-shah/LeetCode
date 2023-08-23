#Beats 96.83%of users with Python
class MinStack(object):

    def __init__(self):
        self.stack = []
        
        self.minlist = [float("Inf")]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val < self.minlist[-1]:
            self.minlist.append(val)
        else:
            self.minlist.append(self.minlist[-1])

        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minlist.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.minlist[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
