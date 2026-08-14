class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        product = 1
        for i in range(len(nums)):
            result.append(product)
            product *= nums[i]

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result