#p proud of this one beats 95.53% of users with Python on runtime
#and 98.43%of users with Python on memory
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        ans = []
        for x in range(len(numbers)):
            for y in range (x + 1, len(numbers)):
                print(str(x) +" --  " + str(y))
                if numbers[x] + numbers[y] == target:
                    
                    ans.append(x + 1)
                    ans.append(y + 1)
                    return ans
                elif numbers[x] + numbers[y] > target:
                    x = y
        '''
        
            
        numset = set(numbers)
        ans = []
        for x in range(-1000, 1000):
            if x in numset and target - x in numset:
                if x == target - x:
                    return [numbers.index(x) + 1, numbers.index(target - x) + 2]
                return [numbers.index(x) + 1, numbers.index(target - x) + 1]
