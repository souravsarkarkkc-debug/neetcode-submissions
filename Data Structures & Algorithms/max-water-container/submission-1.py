class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0
        while i<j:
            
            a = min(heights[i], heights[j])
            b = j-i
            area = a*b
            max_area = max(area,max_area)
            if heights[i]<heights[j]:
                i += 1
            else:
                j-= 1
            
        return (max_area)
        