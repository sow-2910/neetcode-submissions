class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(0,len(nums) - k + 1):
            maxTemp = nums[i]
            for j in range(i, i + k):
                maxTemp = max(maxTemp, nums[j])
            res.append(maxTemp)

        return res
