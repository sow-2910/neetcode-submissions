class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])

        res = [intervals[0]]

        for cur_start, cur_end in intervals:
            last_end = res[-1][1]

            if last_end >= cur_start:
                res[-1][1] = max(last_end, cur_end)
            else:
                res.append([cur_start, cur_end])

        return res

        