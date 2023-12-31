class Solution(object):
    def twoSum(self, nums, target):
        #brute force method - will revist using sets/dictionary later
        '''
        # 0 1 2  3  4.  5  6
        #[3,2, 1, 7, 10, 21,4]
        #print(len(nums))
        for x in range(len(nums)):
            for y in range((x + 1), (len(nums))):
                #print(str(x) + "   " + str(y))
                if nums[x] + nums[y] == target:
                    return [x, y]
        '''
        #much better method - Beats 74.07%of users with Python 
        numset = set(nums)
        for x, num in enumerate(nums):
            if (target - num) in numset and nums.index(target - num) != x:
                return [x, nums.index(target - num)]

        
