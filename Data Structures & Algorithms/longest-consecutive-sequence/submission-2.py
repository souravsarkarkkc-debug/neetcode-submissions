class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        count = 1
        max_count = 1
        for i in range (1 , n):
            if (nums[i] - nums[i-1] == 1):
                count += 1
            elif nums[i] == nums[i-1]:
                continue

            else:
                count = 1

            max_count = max(max_count,count)

        return max_count
                
        