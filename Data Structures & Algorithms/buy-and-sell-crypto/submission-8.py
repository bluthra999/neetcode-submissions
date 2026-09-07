class Solution:
    def maxProfit(self, price: List[int]) -> int:
        
        current_min = price[0]
        profit = 0
       
        for i in range(1,len(price)):
            if price[i-1] < current_min:
                current_min = price[i-1]
            profit = max(profit,price[i]-current_min) 
                
                        

            
        return profit


            


            



        