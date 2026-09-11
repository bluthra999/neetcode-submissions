class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(0,len(strs)):
            l = str(len(strs[i]))
            
            strs[i] = f'{l}#'+strs[i]
            
            

            
        return  "".join(strs)

    def decode(self, s: str) -> List[str]:


        l = []
        j = 0
        while s:
            n = int(s[j:s.index('#')])
            # n = 12 
            l.append(s[s.index('#')+1:n+s.index('#')+1])
            
            s = s[s.index('#')+n+1:]

        return l
