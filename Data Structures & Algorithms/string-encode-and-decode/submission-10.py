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
                gap = i + len(str_length)
                print(gap, len(str_length), s[i])
                str_length = '' #reset
                decoded_str = s[gap : str_count + gap]
                decoded_strs.append(decoded_str)
                i = gap + str_count
            else:
                i += 1
        return decoded_strs