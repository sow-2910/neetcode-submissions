class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = set()
        for i in range(len(nums)):
            if nums[i] in map:
                return nums[i]
            map.add(nums[i])
        return None
