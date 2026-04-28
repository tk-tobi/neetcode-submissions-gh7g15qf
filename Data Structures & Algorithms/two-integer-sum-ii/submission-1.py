class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        #Suboptimal O(n^2) time, O(1) Space
        for i in range(len(numbers) - 1):
            for j in range(i + 1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        '''

        # Using two pointers
        left_ptr = 0
        right_ptr = len(numbers) - 1

        while right_ptr > left_ptr:
            if target > numbers[right_ptr] + numbers[left_ptr]:
                left_ptr += 1
            elif target < numbers[right_ptr] + numbers[left_ptr]:
                right_ptr -= 1
            else:
                return [left_ptr + 1, right_ptr + 1]
        return []
            

        