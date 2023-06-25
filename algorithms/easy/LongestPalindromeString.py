class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        letters = set()
        for ch in s:
            if ch in letters:
                letters.remove(ch)
                result += 2
            else:
                letters.add(ch)
        if letters:
            result += 1

        return result


def getTestData():
    return [
        "abccccdd",
        "a"
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        reversed = list(string)
        solution.reverseString(reversed)
        print("Original string: " + str(string) + " reversed: " + str(reversed))
