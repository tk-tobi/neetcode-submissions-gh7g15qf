class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_store = []
        nums = list(sorted(nums))

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                complement = (nums[i] + nums[j]) * - 1
                if complement in nums[j + 1:]:
                    triplet_store.append([nums[i], nums[j], complement])
                break
        
        return triplet_store
        