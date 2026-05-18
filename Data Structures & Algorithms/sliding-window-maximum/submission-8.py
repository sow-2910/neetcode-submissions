class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # First window start at index 0, but the very last window start at index len(nums) - k
        # So we are counting from index 0 to lens(nums) - k
        for i in range(0, len(nums) - k + 1): #In python the stop is not included, therefore we add one
            maxTemp = nums[i]
            for j in range(i, i + k):
                maxTemp = max(maxTemp, nums[j])
            res.append(maxTemp)

        return res