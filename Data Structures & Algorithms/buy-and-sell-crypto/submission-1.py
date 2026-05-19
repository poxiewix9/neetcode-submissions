class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        minBuy = prices[0]

        for price in prices:
            mProfit = max(mProfit, prices-minBuy)
            minBuy = min(minBuy, price)
        return mProfit