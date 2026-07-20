class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0

        while(i<=j and j < len(prices)):
            if prices[j] - prices[i] < 0:
                i += 1
            else:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
        
        return max_profit
    
s = Solution()
print("Maximum profit : ", s.maxProfit([7,1,5,3,6,4])) # Output: 5