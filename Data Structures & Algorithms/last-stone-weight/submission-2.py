class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = []
        for s in stones:
            new_stones.append(-s)
        stones = new_stones

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])




