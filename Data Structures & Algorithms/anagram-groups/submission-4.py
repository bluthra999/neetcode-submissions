class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = dict()
        
        for i in strs:
            i = ''.join(sorted(i))
            if i in l:
                pass
            else:
                l[''.join(sorted(i))]=len(l)
            
        #  
        bucket = [[] for i in range(len(l))]
        #    
        #  
        for i in strs:
            j = ''.join(sorted(i))
            bucket[l[j]].append(i)         

        
        



        return bucket

	

	
        