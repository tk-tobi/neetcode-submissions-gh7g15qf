class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        starting_index = len(nums) // 2
    
        while 0 < starting_index < len(nums):

            if nums[starting_index] == target:
                return starting_index
                
            elif nums[starting_index] > target:
                starting_index = starting_index // 2

            elif nums[starting_index] < target:
                starting_index = starting_index + starting_index // 2
            return -1
        return -1

        