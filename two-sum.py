class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        result = []
        for index in range(0, len(nums)):
            if target-nums[index] not in d:
                d[nums[index]] = index
            else:
                result = [ d[target-nums[index]], index ]
        return result
