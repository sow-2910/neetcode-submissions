class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (high + low) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        