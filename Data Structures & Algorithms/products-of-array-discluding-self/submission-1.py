class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = []

        # [prefix] [x] [postfix]
        # x = [prefix] * [postfix]

        #prefix
        prefix = []
        prefix_product = 1
        for i in range(len(nums)):
            prefix.append(prefix_product)
            prefix_product *= nums[i]

        #postfix
        postfix = []
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(postfix_product)
            postfix_product *= nums[i]

        postfix.reverse()
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])




        return result