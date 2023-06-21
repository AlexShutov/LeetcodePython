from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s)
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        return -1

def getTestData():
    return [
        "leetcode",
        "loveleetcode",
        "aabb"
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        firstUniqueCharacterPos = solution.firstUniqChar(str)
        print("First unique character position in string " + string + " is: " + str(firstUniqueCharacterPos))
