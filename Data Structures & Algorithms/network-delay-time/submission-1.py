class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w))

        minHeap =[(0, k)]
        visit = set()
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = w1

            for next_n, next_w in edges[n1]:
                if next_n not in visit:
                    heapq.heappush(minHeap, (w1 + next_w, next_n))
        
        return res if len(visit) == n else -1