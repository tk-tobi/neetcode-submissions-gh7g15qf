class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        adder = 0
        for i in range(len(s)):
            adder += ord(s[i])
            adder -= ord(t[i])
        
        return adder == 0