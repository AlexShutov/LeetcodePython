from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterRansom = Counter(ransomNote)
        counterMagazine = Counter(magazine)
        for k, v in counterRansom.items():
            if counterMagazine[k] < v:
                return False

        return True


def getTestData():
    return [
        ("a", "b"),
        ("aa", "ab"),
        ("aa", "aab")
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for ransomNote, magazine in getTestData():
        canBeConstructed = solution.canConstruct(ransomNote, magazine)
        print("Can ransome note " + ransomNote + " be constructed from magazine " + magazine + " ? " + str(
            canBeConstructed))
