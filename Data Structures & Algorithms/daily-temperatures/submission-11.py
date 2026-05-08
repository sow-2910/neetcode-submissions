class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        size = 0
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    size += 1
                    break
            if len(res) <= i:
                res.append(0)
        
        
        return res