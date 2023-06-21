from collections import Counter
from typing import List


def getTestData():
    return [
        ("anagram", "nagaram"),
        ("rat", "car")
    ]


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            if not char in counts:
                counts[char] = 1
            else:
                count = counts[char] + 1
                counts.pop(char)
                counts[char] = count

        for char in t:
            if not char in counts:
                return False
            else:
                count = counts[char]
                count -= 1
                if count == 0:
                    counts.pop(char)
                else:
                    counts[char] = count

        return len(counts) == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for s, t in getTestData():
        isAnagram = solution.isAnagram(s, t)
        print("is " + t + " a valid anagram of " + s + " : " + str(isAnagram))
