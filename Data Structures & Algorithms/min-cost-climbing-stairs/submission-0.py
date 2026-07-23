class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost)

        min_cost = [0, cost[0]]

        for i in range(1, len(cost)):
            mini = min(min_cost[-2] + cost[i], min_cost[-1] + cost[i])
            min_cost.append(mini)
        print(min_cost)
        return min(min_cost[-1], min_cost[-2])
        