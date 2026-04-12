class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)

        for letter in t:
            if letter in s_list:
                s_list.pop(s_list.index(letter))
            else:
                return False
        return True