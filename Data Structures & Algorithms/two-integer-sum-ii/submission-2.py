class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for i,num in enumerate(numbers):
            ans = target - num
            if ans in map:
                if ans < num:
                    return [map[ans] + 1, i + 1]
                else:
                    return [i + 1, map[ans] + 1]
            map[num] = i
        return []