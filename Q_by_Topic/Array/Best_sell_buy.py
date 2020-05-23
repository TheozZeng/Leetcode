class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_min = float("inf")
        max_prof = 0
        for i in prices:
            max_prof = max(max_prof,i - temp_min)
            temp_min = min(i,temp_min)
        return max_prof
