class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_dict = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in complement_dict:
                return [complement_dict[complement], index]
            else:
                complement_dict[nums[index]] = index
        return []
        