class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictForw = {}
        dictBack = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if not charS in dictForw:
                if not charT in dictBack:
                    dictForw[charS] = charT
                    dictBack[charT] = charS
                else:
                    return False
            else:
                if dictForw[charS] != charT or dictBack[charT] != charS:
                    return False

        return True


def getTestData():
    return [
        ("badc", "baba"),
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title")
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for s, t in getTestData():
        isIsomorphic = solution.isIsomorphic(s, t)
        print("Are strings " + s + " and " + t + " isomorphic? " + str(isIsomorphic))
