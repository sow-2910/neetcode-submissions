class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pointerOne = cost[0]
        pointerTwo = cost[1]

        for i in range(2, len(cost)):
            currentMin = cost[i] + min(pointerOne, pointerTwo)
            pointerOne = pointerTwo
            pointerTwo = currentMin

        return min(pointerOne, pointerTwo)
