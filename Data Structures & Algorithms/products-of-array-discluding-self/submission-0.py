class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        left_prod = 1
        for index, value in enumerate(nums):
            result[index] = left_prod
            left_prod *= value
        
        right_prod = 1
        nums.reverse()
        for index, value in enumerate(nums):
            result[index] *= right_prod
            right_prod *= value
        
        return result
