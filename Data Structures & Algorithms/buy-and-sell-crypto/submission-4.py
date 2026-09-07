class Solution:
    def maxProfit(self, price: List[int]) -> int:
        
        
       
        m = 0
        for i in range(len(price)):
            for j in range(i + 1, len(price)):
                m = max(price[j] - price[i], m)
                        

            
        return m


            


            



        