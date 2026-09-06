from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        if nums:
            m= 1
            for i in s:
                x = i
                current_x = x
                current_chain_length = 1
                max_len = 1
                if x-1 not in s:
                    while current_x+1 in s:
                        current_chain_length +=1
                        current_x += 1
                
                
                
                
                m = max(current_chain_length,max_len,m) 
            
            return m
        else:
                return 0

        
   
   


  




        