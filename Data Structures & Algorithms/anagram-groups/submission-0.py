class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {} # {sorted_str : [index]}

        for word in strs:
            new_word = "".join(sorted(word))
            if new_word in anagram_dict:
                anagram_dict[new_word].append(word)
            else:
                anagram_dict[new_word] = [word]
        result = []
        print(anagram_dict)
        for val in anagram_dict.values():
            result.append(val)
        return result
        