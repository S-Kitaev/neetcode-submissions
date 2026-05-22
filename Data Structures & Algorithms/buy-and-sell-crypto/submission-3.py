class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profits = []

        mini = 0
        maxi = 1

        best_mini = 0

        while maxi < len(prices):
            if prices[mini] < prices[best_mini]:
                best_mini = mini

            profit = prices[maxi] - prices[best_mini]
            profits.append(profit)
            if maxi == len(prices) - 1:
                if mini + 1 == maxi:
                    maxi += 1
                else:
                    mini += 1

            else:
                if mini + 1 == maxi:
                    maxi += 1
                elif prices[maxi] <= prices[maxi + 1]:
                    maxi += 1
                elif prices[mini] >= prices[mini+1]:
                    mini += 1
                else:
                    mini += 1

        print(mini, maxi)

        return max(profits) if max(profits) > 0 else 0