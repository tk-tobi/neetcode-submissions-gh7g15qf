class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # move the right pointer
                right = mid - 1
            else:
                # move the left pointer
                left = mid + 1
        return -1