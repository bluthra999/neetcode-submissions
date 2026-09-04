from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = c.most_common(k)
        print(a)
        f = [a[i][0] for i in range(len(a))]


        
        return f