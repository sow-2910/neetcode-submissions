class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        visit = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            cur_w, cur_n = heapq.heappop(minHeap)
            if cur_n in visit:
                continue
            visit.add(cur_n)
            res = cur_w 

            for next_n, next_w in edges[cur_n]:
                if next_n not in visit:
                    heapq.heappush(minHeap, (cur_w + next_w, next_n))
                
        return res if len(visit) == n else -1