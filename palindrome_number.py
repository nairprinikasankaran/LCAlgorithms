# Author: Prinika Sankaran Nair
# LeetCode Link: https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            x * -1
        string = str(x)
        start = 0
        end = len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
