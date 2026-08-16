class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        while left < right:
            mid = (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # move the right pointer
                right = mid - 1
            elif nums[mid] < target:
                # move the left pointer
                left = mid + 1
        return -1