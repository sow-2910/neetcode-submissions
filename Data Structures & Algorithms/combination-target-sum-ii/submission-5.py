class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur_combination, cur_total):
            if cur_total == target:
                res.append(cur_combination.copy())
                return
            if cur_total > target or i >= len(candidates):
                return

            cur_combination.append(candidates[i])
            dfs(i + 1, cur_combination, cur_total + candidates[i])
            cur_combination.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur_combination, cur_total)
        dfs(0, [], 0)

        return res