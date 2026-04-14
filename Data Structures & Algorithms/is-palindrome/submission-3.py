class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "").replace(",", "").replace("'", "").lower().strip('.?')
        reverse_s = "".join([string[i] for i in range(len(string) - 1, -1, -1)])
        
        for i in range(len(string)):
            if string[i] != reverse_s[i]:
                return False
        return True 
        