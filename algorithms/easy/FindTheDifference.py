from collections import Counter


class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        symbolCount = {}
        for ch in s:
            if not ch in symbolCount:
                symbolCount[ch] = 1
            else:
                symbolCount[ch] = symbolCount[ch] + 1

        for ch in t:
            if not ch in symbolCount:
                return ch
            else:
                remainingCount = symbolCount[ch]
                if remainingCount == 1:
                    symbolCount.pop(ch)
                else:
                    symbolCount[ch] = remainingCount - 1
        return ""

    def findTheDifferenceCounter(self, s: str, t: str) -> str:
        counter = Counter(t)
        counter.subtract(Counter(s))
        for k, v in counter.items():
            if v != 0:
                return k


def getTestData():
    return [
        ("abcd", "abcde"),
        ("", "y")
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for s, t in getTestData():
        difference = solution.findTheDifferenceCounter(s, t)
        print("Difference between " + s + " and " + t + " is: " + difference)
