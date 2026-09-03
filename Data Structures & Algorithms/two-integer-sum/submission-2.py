class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           
            d= dict() 
            for i in range(len(nums)):
                a = target - nums[i]
                if a in d.values():
                    return [list(d.values()).index(a),i]
                    
                
                else:
                    d[i] = nums[i]
	
	

            
            
        

            
        