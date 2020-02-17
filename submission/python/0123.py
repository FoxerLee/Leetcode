class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = float('inf')
        price_diff = - float('inf')
        one_profit = two_profit = 0

        for p in prices:

            #first buy 
            #same as problem121
            one_buy = min(one_buy,p)
            one_profit = max(one_profit,p - one_buy)

            # the best time to buy again is,
            # when you have the highest (current_profit - current_price)
            # which means we should maximize price_diff 
            price_diff = max(price_diff, one_profit - p)
            two_profit = max(two_profit, p + price_diff)

            ##the opposite way
            #two_buy = min(two_buy,p - one_profit)
            #two_profit = max(two_profit,p - two_buy)
        return two_profit
