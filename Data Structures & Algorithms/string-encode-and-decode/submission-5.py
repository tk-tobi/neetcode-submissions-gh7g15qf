class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for string in strs:
            coded_str = str(len(string)) + '#' + string
            encoded_str += coded_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []
        i = 0
        str_length = ''
        while i < len(s):
            if s[i].isdigit():
                str_length += s[i]
                i += 1
            elif s[i] == '#' and str_length != '':
                str_count = int(str_length)
                str_length = '' #reset
                decoded_str = s[i + 1 : str_count + i + 1]
                decoded_strs.append(decoded_str)
                i += 1
            else:
                i += 1
        return decoded_strs