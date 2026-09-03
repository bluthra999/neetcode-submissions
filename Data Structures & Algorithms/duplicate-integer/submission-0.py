from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        a =any(value > 1  for value in counter.values())
        
        return a