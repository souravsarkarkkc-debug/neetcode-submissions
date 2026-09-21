class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        n = len(nums)
        suffix = 1
        prefix = 1
        for i in range (n):
            output[i] = suffix
            suffix *= nums[i] 

        for i in range (n-1,-1,-1):
            output[i] *= prefix
            prefix *= nums[i]
        return output