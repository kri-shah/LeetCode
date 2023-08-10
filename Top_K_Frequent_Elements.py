class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1.update({num: 1})
        ans = []
        print(dict1)
        for x in range(k):
            
            ans.append(max(dict1, key=dict1.get))
            del dict1[max(dict1, key=dict1.get)]

        return ans
