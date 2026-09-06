class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        f = True
        i = 0
        j = len(numbers)-1
        while f:
    
            if target == numbers[i]+numbers[j] and i!=j:
                return [i+1,j+1]
            elif target > (numbers[i]+numbers[j]) and i<j:
                i+= 1
            elif target < (numbers[i]+numbers[j]) and i<j:
                j -= 1
                
            elif i == j:
                f = False

    




        