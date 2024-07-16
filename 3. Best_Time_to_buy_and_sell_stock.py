class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # If there are no prices, or only one price, we cannot make any profit
        if not prices or len(prices) == 1:
            return 0

        # Start with the first day's price as the minimum price
        min_price = prices[0]
        # Start with 0 as the maximum profit (since we haven't done any transaction yet)
        max_profit = 0

        # Go through each price starting from the second day
        for price in prices[1:]:
            # Calculate the profit if we sell at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is greater than the previous maximum profit
            if profit > max_profit:
                max_profit = profit
            # Update the minimum price if the current price is lower than the previous minimum price
            if price < min_price:
                min_price = price

        return max_profit


