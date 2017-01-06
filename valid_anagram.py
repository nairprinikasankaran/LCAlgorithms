# Author: Prinika Sankaran Nair
# Link: https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        anadict = {}
        for char in s:
            if char in anadict:
                anadict[char] += 1
            else:
                anadict[char] = 1
        for char2 in t:
            if char2 not in anadict:
                return False
            else:
                anadict[char2] -= 1
                if anadict[char2] == 0:
                    del anadict[char2]
        if anadict == {}:
            return True
