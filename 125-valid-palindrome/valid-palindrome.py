class Solution(object):
    def isPalindrome(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))