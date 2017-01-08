# Author: Prinika Sankaran Nair
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Solution:
        Iterate over range 0 to len(nums), say idx
        if nums[nums[idx]] is > 0
            set element nums[nums[idx]] to -nums[nums[idx]]
        else if already < 0
            this number was seen before hence the nums[idx] is a repeated val
        """
        rep_list = []
        if not nums == []:
            for idx in range(0,len(nums)):
                if nums[abs(nums[idx])-1] > 0:
                    nums[abs(nums[idx])-1] = -1 * nums[abs(nums[idx])-1]
                else:
                    rep_list.append(abs(nums[idx]))
        return rep_list
