from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        c_count = c[0]



        if c_count >= 2:
            return [0]*len(nums)

           
        lst = [x for x in nums if x != 0]


        product = reduce(lambda x, y: x * y, nums)
        product2 = reduce(lambda x, y: x * y, lst)
        num2 = []


        for i in nums:
            try:
                num2.append(product//i)
            except ZeroDivisionError:
                num2.append(product2)
        return num2        
        
        