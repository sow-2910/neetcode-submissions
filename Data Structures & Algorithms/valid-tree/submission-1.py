class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adjList = [[] for i in range(n)]
        visit = set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(currentNode, parentNode):
            if currentNode in visit:
                return False
            visit.add(currentNode)

            for nei in adjList[currentNode]:
                if nei == parentNode:
                    continue
                if not dfs(nei, currentNode):
                    return False
            return True






        return dfs(0, -1) and len(visit) == n