class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], index]
            else:
                complement_dict[num] = index
        return []
        