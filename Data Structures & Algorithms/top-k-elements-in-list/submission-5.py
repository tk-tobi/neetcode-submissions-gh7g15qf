class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}
        freq_list = [[] for num in range(len(nums) + 1)]
        result = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        for key, value in freq_dict.items():
            freq_list[value].append(key)
        
        for i in range(len(nums), 0, -1):
            result += freq_list[i]
            if len(result) == k:
                return result
        return result
        

