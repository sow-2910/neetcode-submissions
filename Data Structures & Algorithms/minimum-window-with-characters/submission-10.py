class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res = ""
        minLen = float("infinity")

        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                isValid = True
                for c in countT:
                    if countS.get(c,0) < countT[c]:
                        isValid = False
                        break
                if isValid and (j - i + 1) < minLen:
                    minLen = j - i + 1
                    res = s[i : j + 1]

        return res
