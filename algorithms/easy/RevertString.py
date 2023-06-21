from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def getTestData():
    return [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        reversed = list(string)
        solution.reverseString(reversed)
        print("Original string: " + str(string) + " reversed: " + str(reversed))
