# Author: Prinika Sankaran Nair
# LeetCode Link:https://leetcode.com/problems/valid-number/

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dot = False
        s = s.lstrip()
        s = s.rstrip()
 
        if s == "" or s == ".":
            return False
        try:
            float(s)
        except:
            return False
        else:
            return True
