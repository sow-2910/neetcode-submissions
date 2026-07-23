class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #This return a harsh map where keys are characters and values are their repetitions in the given array tasks
        maxHeap = [-cnt for cnt in count.values()] #trick to turn a minHeap to a maxHeap in Python
        heapq.heapify(maxHeap)

        q = deque() #pairs [cnt, idle time]
        time = 0

        while maxHeap or q: 
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: #Check whether cnt != 0
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time 




