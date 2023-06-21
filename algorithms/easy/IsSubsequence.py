class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = list(s)
        for char in t:
            if len(queue) != 0 and queue[0] == char:
                queue.pop()
        return len(queue) == 0

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


def getTestData():
    return [("abc", "ahbgdc"), ("axc", "ahbgdc")]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for (s, t) in getTestData():
        isSubsequence = solution.isSubsequence(s, t)
        print("is " + s + " subsequence of " + t + " : " + str(isSubsequence))
