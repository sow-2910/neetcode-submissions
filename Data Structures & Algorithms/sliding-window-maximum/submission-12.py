class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = deque()
        while r < len(nums) :
            # If the q is not empty, and the number we add to the queue is 
            # larger than the number that currently in the window. We pop it out
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # If the position of the beginning of the window is larger than
            # the position of the biggest number currently in the queue. We pop it out
            if l > q[0]:
                q.popleft()
            
            # if reach the size of the window aka the given k, we add it to our res
            # k + 1 since index is begin from 0
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res