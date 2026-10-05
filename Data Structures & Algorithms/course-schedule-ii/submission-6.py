class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: []  for c in range(numCourses)}

        for c, pre in prerequisites:
            preMap[c].append(pre)

        output = []
        visiting, visited = set(), set();

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            
            visiting.add(c)
            for pre in preMap[c]:
                if (dfs(pre) == False):
                    return False
            
            visiting.remove(c)
            visited.add(c)
            output.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output