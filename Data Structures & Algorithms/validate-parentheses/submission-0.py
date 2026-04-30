class Solution:
    def isValid(self, s: str) -> bool:

        open_bracket = ['(', '[', '{']
        close_bracket = {')': '(', ']': '[', '}':'{'}

        stack = []
        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif char in close_bracket.keys():
                if stack.pop() != close_bracket[char]:
                    return False

        return True
            


        