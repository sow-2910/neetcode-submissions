class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            mySet = set()
            for j in range(i+1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in mySet:
                    res.add((nums[i], target, nums[j]))
                mySet.add(nums[j])
        return [list(t) for t in res]