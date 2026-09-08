class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        area = 0
        while j>i:
        
            width = j - i 
            height = min(nums[j],nums[i])
            area  = max(width* height,area)
            if nums[j]>nums[i]:
                i += 1
            else:
                j -= 1 
        
        return area