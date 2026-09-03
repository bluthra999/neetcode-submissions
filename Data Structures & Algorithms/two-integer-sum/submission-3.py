class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            if len(nums) == 2:
                return [0,1]
            d= dict() 
            for i in range(len(nums)):
                a = target - nums[i]
                if a in d:
                    return [list(d).index(a),i]
                    
                
                else:
                    d[nums[i]] = i
	
	

            
            
        

            
        