class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        hashSet = set()
        currentSize = 0
        result = []

        for c in s:
            hashMap[c] = 1 + hashMap.get(c, 0)

        for c in s:
            hashSet.add(c)
            hashMap[c]-= 1
            currentSize += 1

            if hashMap[c] == 0:
                hashSet.remove(c)
            
            if not hashSet:
                result.append(currentSize)
                currentSize = 0

        return result
