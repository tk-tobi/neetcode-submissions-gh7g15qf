class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_store = []
        nums.sort()

        i = 0
        while i  < (len(nums) - 2):
            if nums[i] == nums[i + 1]:
                i += 1
            for j in range(i + 1, len(nums) - 1):
                for k in range(i + 2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet_store.append([nums[i], nums[j], nums[k]])
                i += 1
        
        return triplet_store
        