# Author: Prinika Sankaran Nair
# Link: https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        for element in nums:
            if element not in rlist:
                rlist.append(element)
            else:
                rlist.remove(element)
        return rlist
