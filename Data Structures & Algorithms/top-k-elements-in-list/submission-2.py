class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}
        result = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        for key, value in freq_dict.items():
            if value >= k:
                result.append(key)
        #if len(result) == 0:
        #    result = nums
        return result